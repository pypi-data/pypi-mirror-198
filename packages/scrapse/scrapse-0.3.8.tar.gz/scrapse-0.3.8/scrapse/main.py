import typer

from typing import Optional
from pathlib import Path
from scrapse.leggitalia.leggitalia import leggitalia_app

__version__ = "0.3.8"

app = typer.Typer()
app.add_typer(leggitalia_app, name='leggitalia')


def version_callback(value: bool):
    if value:
        print(f"ScrapSE {__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None, '--version', '-v', callback=version_callback
        )):
    """
        Package created for the extraction of judgments.
    """
    main_directory_path = Path('/'.join((str(Path.home()), 'scrapse')))
    main_directory_path.mkdir(exist_ok=True, parents=True)


if __name__ == "__main__":
    app()
