import typer
import requests
import json

from scrapse.leggitalia.utils import LeggiDiItalia
from rich.progress import Progress, SpinnerColumn, TextColumn


def extract_voices(ldi, key=None):
    request = requests.post(url=ldi.baseurl, headers=ldi.headers,
                            params=ldi.build_export_voices_query(key=key))
    voices = request.json()['result']['content']
    for voice in voices:
        if 'folder' in voice:
            del voice['folder']
            voice['items'] = extract_voices(ldi, key=voice['key'])
    return voices


def scrap_voices(
        path: str = typer.Option(LeggiDiItalia.main_directory_path, '--path', '-p',
                                 help='Path where to save json file'),
        show: bool = typer.Option(True, '--show', '-s', help='View extracted voices.')
):
    """
        Extraction of the voices tree
    """
    ldi = LeggiDiItalia(path=path, command='scrap_voices')
    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=False,
    ) as progress:
        progress.add_task(description="Extraction of voices...", total=None)
        voices = json.dumps(extract_voices(ldi))
        json_file = open('/'.join([str(path), 'leggitalia_albero_voci.json']), 'w')
        json_file.write(voices)
        json_file.close()
    progress.console.print(f'\u2713 successfully extracted')
