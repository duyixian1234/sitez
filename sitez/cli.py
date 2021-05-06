import typer

from sitez import __version__

from .commands import init_project

app = typer.Typer(name="sitez", no_args_is_help=True)


@app.command("version")
def describe_version() -> None:
    typer.echo(f"Sitez version: {__version__}")


@app.command("init")
def init(path: str) -> None:
    init_project(path)
    typer.echo(f"Init sitez project at {path}")


def run():
    app()
