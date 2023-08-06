
import click
import coloredlogs, logging
import os, sys
import yaml

from stackdiac.models import stackd

logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')

@click.command()
def run():
    click.echo("stackd is workin")

@click.command()
def run_all():
    click.echo("stackd is workin")


@click.command()
@click.option("-p", "--path", default=".", show_default=True, help="project directory")
def update(path, **kwargs):
    sd = stackd.Stackd(root=path)
    sd.download_binaries()
    sd.update()

@click.command()
@click.option("-p", "--path", default=".", show_default=True, help="project directory")
@click.argument("target")
def plan(path, target, **kwargs):
    sd = stackd.Stackd(root=path)
    sd.plan(target, **kwargs)

@click.group()
def cli():
    pass


from .init import init
from .build import build

cli.add_command(init)
cli.add_command(build)
cli.add_command(plan)
cli.add_command(update)
