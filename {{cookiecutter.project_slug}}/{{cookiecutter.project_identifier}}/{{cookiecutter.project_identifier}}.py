import click
from vpype import LineCollection, generator


@click.command()
@generator
def {{cookiecutter.command_name}}():
    """
    Insert documentation here...
    """
    lc = LineCollection()
    return lc


{{cookiecutter.command_name}}.help_group = "Plugins"
