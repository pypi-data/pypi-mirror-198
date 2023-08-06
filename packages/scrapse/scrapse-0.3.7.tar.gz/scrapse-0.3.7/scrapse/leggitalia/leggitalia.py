import typer

from pathlib import Path
from scrapse.leggitalia.commands import scrap_judgments
from scrapse.leggitalia.commands import dump_judgments
from scrapse.leggitalia.commands import scrap_voices
from scrapse.leggitalia.commands import save_cookie
from scrapse.leggitalia.commands import show_filters

leggitalia_app = typer.Typer()
leggitalia_app.command()(scrap_judgments.scrap_judgments)
leggitalia_app.command()(dump_judgments.dump_judgments)
leggitalia_app.command()(scrap_voices.scrap_voices)
leggitalia_app.command()(save_cookie.save_cookie)
leggitalia_app.command()(show_filters.show_filters)


@leggitalia_app.command()
def show_voices():
    """
    Shows the tree of voices
    """
    pass


@leggitalia_app.callback()
def callback():
    """Dedicated command to the site LEGGI D'ITALIA PA"""
    main_directory_path = Path('/'.join([str(Path.home()), 'scrapse', 'leggitalia']))
    main_directory_path.mkdir(exist_ok=True, parents=True)


if __name__ == "__main__":
    leggitalia_app()
