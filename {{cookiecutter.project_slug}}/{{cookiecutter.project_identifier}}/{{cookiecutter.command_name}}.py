import vpype as vp
import vpype_cli


@vpype_cli.cli.command(group="Plugins")
@vpype_cli.generator
def {{cookiecutter.command_name}}() -> vp.LineCollection:
    """
    Insert documentation here...
    """
    lc = vp.LineCollection()
    return lc
