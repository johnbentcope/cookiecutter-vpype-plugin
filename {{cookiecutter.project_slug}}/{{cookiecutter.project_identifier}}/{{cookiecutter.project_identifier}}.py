import click
import vpype as vp
import vpype_cli


@click.command()
@vpype_cli.generator
def {{cookiecutter.command_name}}():
    """
    Insert documentation here...
    """
    lc = vp.LineCollection()
    return lc


{{cookiecutter.command_name}}.help_group = "Plugins"
