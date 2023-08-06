import click
from pyfiglet import Figlet

from openkoppeltaal import __version__ as VERSION
from openkoppeltaal.settings import CommandLineArgs, load_settings, merge_config

font = Figlet(font="smslant", width=88)


class OkptAsyncRunner:
    def __init__(self, config, debug):
        self.config = config


class OkptCli:
    def __init__(self, **kwargs):
        # Get commandline arguments
        self.args = CommandLineArgs(**kwargs)
        # Get toml file settings
        self.toml_config = load_settings(self.args.config)
        # build config
        self.config = merge_config(self.toml_config, self.args.dict())
        # build runner
        self.runner = OkptAsyncRunner(self.config, self.args.debug)

    def show_version(self, noverbose) -> None:
        if not noverbose:
            click.secho("openkoppeltaal CLI tools")
            click.secho(font.renderText("OKPT"), fg="white")
            click.secho(f"Version {VERSION}")
        else:
            click.secho(VERSION)


pass_okpt = click.make_pass_decorator(OkptCli, ensure=True)
