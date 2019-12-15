import click
from vpype import generator, LineCollection

@click.command()
@generator
def {{cookiecutter.project_identifier}}():
    """
    Insert documentation here...
    """
    lc = LineCollection()
    return lc