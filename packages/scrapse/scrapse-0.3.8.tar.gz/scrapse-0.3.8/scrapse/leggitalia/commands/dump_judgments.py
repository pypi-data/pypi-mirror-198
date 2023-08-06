import json
import os
import typer
import re

from rich.progress import Progress, BarColumn, TimeRemainingColumn, TimeElapsedColumn
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from scrapse.leggitalia.utils import LeggiDiItalia, Judgment, JudgmentMetadata, JudgmentCorpus, JudgmentEncoder, \
    SECTIONS


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


def extract_metadata_and_corpus(file):
    soup = read_file(file)
    file_name = file.split('/')[-1].split('.')[0]
    judgment_metadata = extract_metadata(soup, file_name)
    judgment_corpus = extract_corpus(soup, file_name)
    return judgment_metadata, judgment_corpus


def build_dict(metadata_and_corpus):
    metadata_dict, corpus_dict = dict(), dict()
    for metadata, corpus in metadata_and_corpus:
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

    return metadata_dict, corpus_dict


def save_json_mongodb(dictionary, path, directory):
    path.joinpath(directory).mkdir(exist_ok=True, parents=True)
    for tribunale_key in dictionary.keys():
        for sent_anno_key, value in dictionary[tribunale_key].items():
            full_path = '/'.join([str(path), directory, f'{tribunale_key}_{sent_anno_key}.json'])
            with open(full_path, 'w') as f:
                f.write(json.dumps([data for data in value], cls=JudgmentEncoder, indent=4, ensure_ascii=False))


def save_json_unified(unified_judgments, path):
    full_path = '/'.join([str(path), 'unified.json'])
    with open(full_path, 'w') as f:
        f.write(json.dumps([data for data in unified_judgments], cls=JudgmentEncoder, indent=4, ensure_ascii=False))


def dump_judgments(
        directory: str = typer.Option(None, '--directory', '-d', help='Folder path from which to read judgments.',
                                      show_default=False),
        extension: str = typer.Option('HTM', '--extension', '-e', help='File extension to read.'),
        path: str = typer.Option('/'.join([LeggiDiItalia.main_directory_path, 'judgments_dump']), '--path', '-p',
                                 help='Folder path from which to read judgments.'),
        mongo: bool = typer.Option(False, '--mongodb', '-m', help='Dump judgments for mongoDB'),
        unified: bool = typer.Option(False, '--unified', '-u', help='Dump judgments into unified json file'),
):
    """
    Dump judgments to json format
    """

    if mongo or unified:
        with Progress(
                "[progress.description]{task.description}",
                BarColumn(),
                "[progress.percentage]{task.percentage:>3.0f}%",
                TimeRemainingColumn(),
                TimeElapsedColumn(),
                refresh_per_second=5,
        ) as progress:
            files_to_read = ['/'.join([directory, filename]) for filename in os.listdir(directory) if
                             filename.endswith(extension)]
            progress_task = progress.add_task(description="[green]Extract metadata and corpus progress",
                                              total=len(files_to_read), completed=0)

            metadata_and_corpus = list()
            with ThreadPoolExecutor() as executor:
                for index, file in enumerate(files_to_read[:100]):
                    metadata_and_corpus.append(executor.submit(extract_metadata_and_corpus, file).result())
                    progress.update(progress_task, completed=index)

            if mongo:
                progress.update(progress_task, description="[green]Save json for MongoDB progress", total=3,
                                completed=0)
                dump_judgments_directory_path = Path(
                    '/'.join([path, f'mongodb_{datetime.now().strftime("%d-%Y_%H-%M-%S")}']))
                dump_judgments_directory_path.mkdir(exist_ok=True, parents=True)
                progress.update(progress_task, completed=1)
                metadata_dict, corpus_dict = build_dict(metadata_and_corpus)
                progress.update(progress_task, completed=2)

                with ThreadPoolExecutor() as executor:
                    executor.submit(save_json_mongodb, metadata_dict, dump_judgments_directory_path, 'metadata')
                    executor.submit(save_json_mongodb, corpus_dict, dump_judgments_directory_path, 'corpus')
                progress.update(progress_task, completed=3)

            if unified:
                progress.update(progress_task, description="[green]Save unified json progress", total=3, completed=0)
                dump_judgments_directory_path = Path(
                    '/'.join([path, f'unified_{str(datetime.now().strftime("%d-%Y_%H-%M-%S"))}']))
                dump_judgments_directory_path.mkdir(exist_ok=True, parents=True)
                progress.update(progress_task, completed=1)

                unified_judgments = [Judgment(metadata=metadata, corpus=corpus) for metadata, corpus in
                                     metadata_and_corpus]
                progress.update(progress_task, completed=2)
                save_json_unified(unified_judgments, dump_judgments_directory_path)
                progress.update(progress_task, completed=3)
    else:
        print('No specification of json type (mongodb or unified).\nUse --help for more info.')
        raise typer.Exit()
