import click
from vpype.model import LineCollection
from vpype.decorators import generator


@click.command()
@generator
def {{cookiecutter.command_name}}():
    """
    Insert documentation here...
    """
    lc = LineCollection()
    return lc


{{cookiecutter.command_name}}.help_group = "Plugins"
