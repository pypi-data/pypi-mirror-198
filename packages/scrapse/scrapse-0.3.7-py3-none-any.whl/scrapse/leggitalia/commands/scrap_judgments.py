import typer
import requests
import math

from scrapse.leggitalia.utils import LeggiDiItalia, SECTIONS
from pathlib import Path
from bs4 import BeautifulSoup
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeRemainingColumn, TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor


def extract_file_name(soup, judgment_id):
    estrcomp = soup.find('div', class_='estrcomp')
    file_name = estrcomp.text.lower().split(
        [section.strip().lower() for section in SECTIONS if section in estrcomp.text][0], 1)[0].strip() + judgment_id
    file_name = file_name.replace(' ', '').replace('tribunale', '')
    return file_name


def search_judgments(ldi):
    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=False,
    ) as progress:
        progress.add_task(description="Searching for judgments...", total=None)
        request = requests.post(url=ldi.baseurl, headers=ldi.headers,
                                params=ldi.search_judgment_params)
    judgments_found = request.json()['result']['rows']
    progress.console.print(f'\u2713 Found {judgments_found} judgments')
    return typer.prompt('How many judgments do you want to download?', default=judgments_found, type=int)


def build_pagination(ldi, judgments_to_download):
    pagination = list()
    for index in range(0, math.ceil(judgments_to_download / ldi.batch_size), 1):
        start = index * ldi.batch_size
        rows = ldi.batch_size if (judgments_to_download - (
                (index + 1) * ldi.batch_size)) >= 0 else judgments_to_download - (ldi.batch_size * index)

        pagination.append((start, rows))
    # print(pagination)
    return pagination


def export_judgments_id(ldi, page):
    request = requests.post(url=ldi.baseurl, headers=ldi.headers, params=ldi.pagination_query(page))
    return request.json()['result']['items']


def export_judgments(ldi, items):
    judgments_id = [judgment['id'] for judgment in items]

    formatted_judgments_id = ['|'.join(judgments_id[i:i + ldi.batch_size]) for i in
                              range(0, len(judgments_id), ldi.batch_size)]

    request = requests.post(url=ldi.baseurl, headers=ldi.headers, params=ldi.build_export_query(formatted_judgments_id))

    soup = BeautifulSoup(request.text, 'html.parser')
    for index, judgment in enumerate(soup.find_all("div", {"class": "doc_body"})):
        output_file = Path('/'.join(
            (f'{ldi.judgment_directory_path}', f'{extract_file_name(judgment, judgments_id[index])}.{ldi.extension}')))
        output_file.write_text(str(judgment))


def scrap_judgments(
        judicial_bodies: str = typer.Option(None, "--judicial-bodies", "-j", help="Filter judging bodies"),
        location: str = typer.Option(None, "--location", "-l", help="Filter location of the court of reference"),
        sections: str = typer.Option(None, "--sections", "-s", help="Reference section filter, may change by location"),
        path: Path = typer.Option(LeggiDiItalia.main_directory_path, "--path", "-p",
                                  help="Path where to save downloaded judgments"),
        extension: str = typer.Option("HTM", "--extension", "-e", help="Desired extension of judgments"),
):
    """
        Extract the judgments from the platform https://pa.leggiditalia.it """'\n'"""
        It is necessary to specify at least one filter among: -j, -l and -s. """'\n'"""
        Provide an input list with the following formatting: -s 'par1, par2, ...'
    """
    ldi = LeggiDiItalia(judicial_bodies=judicial_bodies, location=location, sections=sections,
                        path=path, extension=extension, command='scrap_judgments')
    number_of_judgments = search_judgments(ldi)
    pagination = build_pagination(ldi, number_of_judgments)

    with Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeRemainingColumn(),
            TimeElapsedColumn(),
            refresh_per_second=5,
    ) as progress:
        futures = []
        overall_progress_task = progress.add_task(description="[green]Extraction of all judgments",
                                                  total=len(pagination))
        with ThreadPoolExecutor() as executor:
            for index, page in enumerate(pagination):
                judgments_id = export_judgments_id(ldi, page)
                futures.append(executor.submit(export_judgments, ldi, judgments_id))
                progress.update(overall_progress_task, completed=index)
            while (n_finished := sum([future.done() for future in futures])) < len(futures):
                progress.update(overall_progress_task, completed=n_finished + 1)
