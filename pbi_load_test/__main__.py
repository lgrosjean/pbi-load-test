import click

from pbi_load_test import __version__
from pbi_load_test.pbi import PowerBIClient
from pbi_load_test.run import run as _run


@click.group(invoke_without_command=True)
@click.option("-v", "--version", required=False, is_flag=True)
def cli(version):
    """Application to simplify Power BI Load Test."""
    ctx = click.get_current_context()
    if ctx.invoked_subcommand is None:
        if version:
            click.echo(__version__)
        else:
            click.echo(ctx.get_help())


@cli.command()
def token():
    pbi_client = PowerBIClient()
    click.echo(pbi_client.token, color=True)


@cli.command()
@click.option("--keep", is_flag=True, help="Keep the created temporary files")
@click.option("--show", is_flag=True, help="Show Chromium driver")
def run(keep, show):
    _run(clean=not keep, headless=not show)


if __name__ == "__main__":
    cli()
