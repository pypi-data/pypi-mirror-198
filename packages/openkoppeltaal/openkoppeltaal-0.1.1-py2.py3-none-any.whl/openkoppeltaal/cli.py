import click

from openkoppeltaal.commands import OkptCli, pass_okpt


@click.group()
@click.option("--debug", is_flag=True, help="enable debug logs")
@click.option("--config", default="okpt.toml", help="custom config file")
@click.pass_context
def cli(ctx, **kwargs):
    """openkoppeltaal command line tools"""
    ctx.obj = OkptCli(**kwargs)


@cli.command("version", short_help="show openkoppeltaal version")
@click.option(
    "--noverbose", is_flag=True, help="no logo and header, only version_number"
)
@pass_okpt
def version(okpt, **kwargs):
    okpt.show_version(**kwargs)


if __name__ == "__main__":
    cli()
