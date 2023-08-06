import os
import typer
import re

from rich.progress import Progress, BarColumn, TimeRemainingColumn, TimeElapsedColumn
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from scrapse.leggitalia.utils import LeggiDiItalia, Judgment, JudgmentMetadata, JudgmentCorpus, SECTIONS


def read_file(path):
    # print(path)
    with open(path, 'r') as file:
        return BeautifulSoup(file, 'html.parser')


def extract_file_name(soup):
    file_name = soup.find('div', class_='estrcomp')
    return ''.join(token for token in file_name.text if token.isalnum())


def extract_voices(soup):
    voices = list()
    spans = soup.find('div', class_='sent_classificazione').find_all('span', class_=True)
    split = list()
    for index, span in enumerate(spans[:-1]):
        if span['class'][0].split('_')[2] > spans[index + 1]['class'][0].split('_')[2]:
            split.append(index + 1)

    split_spans = [[span for span in spans[s:e]] for s, e in zip([0] + split, split + [None])]
    for spans in split_spans:
        classification = ''
        if len(spans) > 1:
            for index, span in enumerate(spans[:-1]):
                if span['class'] < spans[index + 1]['class']:
                    classification += span.text + '/' if (index < len(spans[:-1]) - 1) \
                        else span.text + '/' + spans[index + 1].text
                elif span['class'] == spans[index + 1]['class']:
                    classification += span.text + '_' if (index < len(spans[:-1]) - 1) \
                        else span.text + '_' + spans[index + 1].text
        else:
            classification += spans[0].text
        voices.append(classification)
        # print(voices)
    return voices


def extract_object(soup):
    keyword = 'oggetto:'
    tag = soup.find(text=lambda t: t and keyword in t.lower())
    return tag.parent.text.replace('(asterisco)', '').lower().split(keyword, 1)[1].strip() if tag is not None else None


def extract_tribunal_section(soup):
    estrcomp = soup.find('div', class_='estrcomp')
    section = [section.strip().lower() for section in SECTIONS if section in estrcomp.text][0]
    tribunal = estrcomp.text.lower().split(section, 1)[0].strip()
    # print(f'tribunale {tribunal}')
    # print(f'section {section}')
    return tribunal, section


def extract_sent_anno(soup):
    text = soup.find('div', class_='estrcomp').text
    match_date = re.search(r'\d{2}/\d{2}/\d{4}', text)
    return datetime.strptime(match_date.group(), '%d/%m/%Y').year


def extract_metadata(soup):
    extract_sent_anno(soup)
    tribunale, sezione = extract_tribunal_section(soup)
    judgment_metadata = JudgmentMetadata(
        nomefile=extract_file_name(soup),
        origine='onelegale',
        tribunale=tribunale,
        sezione=sezione,
        voci=extract_voices(soup),
        sent_anno=extract_sent_anno(soup)
    )
    return judgment_metadata


def extract_corpus(soup):
    corpus = dict()

    menu_items = [item['href'].replace('#', '') for item in
                  soup.find('div', class_='sent_menu').find_all('a', href=True)]

    current_key = ''
    for element in soup.find('a', id=menu_items[0]).parent.next_elements:
        if element.name == 'a' and element['id'] in menu_items:
            if element['id'] == 'diritto':
                current_key = 'decisione'
            elif element['id'] == 'dispositivo':
                current_key = 'pqm'
            elif element['id'] == 'fatto-diritto':
                current_key = 'fatto-decisione'
            else:
                current_key = element['id']
            corpus[current_key] = list()
        elif element.name == 'p':
            corpus[current_key].append(element.text.strip())

    for key, value in corpus.items():
        if value is not None:
            corpus[key] = ' '.join(corpus[key])

    judgment_corpus = JudgmentCorpus(
        oggetto=extract_object(soup),
        fatto=corpus.get('fatto'),
        decisione=corpus.get('decisione'),
        fatto_decisione=corpus.get('fatto-decisione'),
        pqm=corpus.get('pqm'),
    )

    return judgment_corpus


def save_json(file, dump_directory):
    soup = read_file(file)
    judgment_metadata = extract_metadata(soup)
    judgment_corpus = extract_corpus(soup)
    judgment = Judgment(metadata=judgment_metadata, corpus=judgment_corpus)

    full_path = '/'.join([str(dump_directory), f'{judgment.metadata.nomefile}.json'])
    with open(full_path, 'w') as f:
        f.write(judgment.toJSON())


def dump_judgments(
        directory: str = typer.Option(None, '--directory', '-d', help='Folder path from which to read judgments.',
                                      show_default=False),
        file: str = typer.Option(None, '--file', '-f', help='Path to the file to read.', show_default=False),
        extension: str = typer.Option('HTM', '--extension', '-e', help='File extension to read.'),
        path: str = typer.Option('/'.join([LeggiDiItalia.main_directory_path, 'judgments_dump']), '--path', '-p',
                                 help='Folder path from which to read judgments.'),
):
    """
    Dump judgments to json format
    """
    judgments_dump_directory_path = Path(path)
    judgments_dump_directory_path.mkdir(exist_ok=True, parents=True)

    files_to_read = ['/'.join([directory, filename]) for filename in os.listdir(directory) if
                     filename.endswith(extension)] if directory is not None else [file]

    with Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeRemainingColumn(),
            TimeElapsedColumn(),
            refresh_per_second=5,
    ) as progress:
        futures = []
        overall_progress_task = progress.add_task(description="[green]Dump progress",
                                                  total=len(files_to_read))

        with ThreadPoolExecutor() as executor:
            for index, file in enumerate(files_to_read):
                futures.append(executor.submit(save_json, file, judgments_dump_directory_path))
            while (n_finished := sum([future.done() for future in futures])) < len(futures):
                progress.update(overall_progress_task, completed=n_finished)
