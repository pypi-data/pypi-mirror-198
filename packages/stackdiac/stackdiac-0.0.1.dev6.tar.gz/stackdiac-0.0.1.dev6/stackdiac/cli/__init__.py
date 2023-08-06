
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


    

@click.group()
def cli():
    pass


from .create import create
from .build import build

cli.add_command(create)
cli.add_command(build)
cli.add_command(update)

TERRAGRUNT_COMMANDS = [
    "apply", "init", "plan", "destroy", "run-all", "output"
]

def get_cmd(tg_cmd):
    @click.command(context_settings={"ignore_unknown_options": True}, name=tg_cmd)
    @click.option("-p", "--path", default=".", show_default=True, help="project directory")
    @click.argument("target")
    @click.argument("terragrunt_options", nargs=-1)
    def _cmd(path, target, terragrunt_options, **kwargs):
        stackd.Stackd(root=path).terragrunt(target, [tg_cmd, *terragrunt_options], **kwargs)
    return _cmd

for tg_cmd in TERRAGRUNT_COMMANDS:
    cli.add_command(get_cmd(tg_cmd))


