import click
import vpype as vp


@click.command()
@vp.generator
def {{cookiecutter.command_name}}():
    """
    Insert documentation here...
    """
    lc = vp.LineCollection()
    return lc


{{cookiecutter.command_name}}.help_group = "Plugins"
