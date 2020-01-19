import click
from vpype.model import LineCollection
from vpype.decorators import generator

@click.command()
@generator
def {{cookiecutter.project_identifier}}():
    """
    Insert documentation here...
    """
    lc = LineCollection()
    return lc

{{cookiecutter.project_identifier}}.help_group = "Plugins"