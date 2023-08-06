import json
import os
import typer
import re

from rich.progress import Progress, BarColumn, TimeRemainingColumn, TimeElapsedColumn
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from scrapse.leggitalia.utils import LeggiDiItalia, JudgmentMetadata, JudgmentCorpus, SECTIONS


def read_file(path):
    # print(path)
    with open(path, 'r') as file:
        return BeautifulSoup(file, 'html.parser')


def extract_voices(soup):
    voices = None
    div_class = soup.find('div', class_='sent_classificazione')
    if div_class is not None:
        voices = list()
        split = list()
        spans = div_class.find_all('span', class_=True)
        for index, span in enumerate(spans[:-1]):
            if span['class'][0].split('_')[2] > spans[index + 1]['class'][0].split('_')[2]:
                split.append(index + 1)
            elif span['class'][0].split('_')[2] == 'l1' and spans[index + 1]['class'][0].split('_')[2] == 'l1':
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
    tribunal = estrcomp.text.lower().split(section, 1)[0].replace('tribunale', '').strip()
    # print(f'tribunale {tribunal}')
    # print(f'section {section}')
    return tribunal, section


def extract_sent_anno(soup):
    text = soup.find('div', class_='estrcomp').text
    match_date = re.search(r'\d{2}/\d{2}/\d{4}', text)
    return datetime.strptime(match_date.group(), '%d/%m/%Y').year


def extract_metadata(soup, file_name):
    extract_sent_anno(soup)
    tribunale, sezione = extract_tribunal_section(soup)
    judgment_metadata = JudgmentMetadata(
        nomefile=file_name,
        origine='onelegale',
        tribunale=tribunale,
        sezione=sezione,
        voci=extract_voices(soup),
        sent_anno=extract_sent_anno(soup),
        tipo='sentenza di merito'
    )
    return judgment_metadata


def extract_corpus(soup, file_name):
    corpus = dict()

    menu_items = [item['href'].replace('#', '') for item in
                  soup.find('div', class_='sent_menu').find_all('a', href=True)]

    current_key = None
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
        nomefile=file_name,
        oggetto=extract_object(soup),
        fatto=corpus.get('fatto'),
        decisione=corpus.get('decisione'),
        fatto_decisione=corpus.get('fatto-decisione'),
        pqm=corpus.get('pqm'),
    )

    return judgment_corpus


def extract_json(soup, file):
    file_name = file.split('/')[-1].split('.')[0]
    judgment_metadata = extract_metadata(soup, file_name)
    judgment_corpus = extract_corpus(soup, file_name)
    return judgment_metadata, judgment_corpus


def build_dict(file, metadata_dict, corpus_dict):
    metadata, corpus = extract_json(read_file(file), file)
    tribunale_key = metadata.tribunale.replace(' ', '_')
    sent_anno_key = str(metadata.sent_anno)

    if metadata_dict.get(tribunale_key) is None:
        metadata_dict[tribunale_key] = dict()
        corpus_dict[tribunale_key] = dict()
    if metadata_dict.get(tribunale_key).get(sent_anno_key) is None:
        metadata_dict[tribunale_key][sent_anno_key] = list()
        corpus_dict[tribunale_key][sent_anno_key] = list()

    metadata_dict[tribunale_key][sent_anno_key].append(metadata)
    corpus_dict[tribunale_key][sent_anno_key].append(corpus)


def save_json(dict, path, directory):
    path.joinpath(directory).mkdir(exist_ok=True, parents=True)
    for tribunale_key in dict.keys():
        for sent_anno_key, value in dict[tribunale_key].items():
            full_path = '/'.join([str(path), directory, f'{tribunale_key}_{sent_anno_key}.json'])
            with open(full_path, 'w') as f:
                f.write(json.dumps([metadata.__dict__ for metadata in value], indent=4, ensure_ascii=False))


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
    with Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeRemainingColumn(),
            TimeElapsedColumn(),
            refresh_per_second=5,
    ) as progress:
        dump_judgments_directory_path = Path(path)
        dump_judgments_directory_path.mkdir(exist_ok=True, parents=True)

        files_to_read = ['/'.join([directory, filename]) for filename in os.listdir(directory) if
                         filename.endswith(extension)] if directory is not None else [file]
        metadata_dict, corpus_dict = dict(), dict()

        progress_task = progress.add_task(description="[green]Dump progress", total=len(files_to_read))

        for index, file in enumerate(files_to_read):
            build_dict(file, metadata_dict, corpus_dict)
            progress.update(progress_task, completed=index)

        with ThreadPoolExecutor() as executor:
            executor.submit(save_json, metadata_dict, dump_judgments_directory_path, 'metadata')
            executor.submit(save_json, corpus_dict, dump_judgments_directory_path, 'corpus')
