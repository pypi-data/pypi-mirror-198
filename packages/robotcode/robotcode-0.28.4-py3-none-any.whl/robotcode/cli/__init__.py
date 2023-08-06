from pathlib import Path
from typing import Optional

import click

from robotcode.plugin.manager import PluginManager

from .__version__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=False)
@click.version_option(version=__version__, prog_name="robotcode")
@click.option(
    "--config",
    "config_file",
    type=click.Path(exists=True, path_type=Path),
    help="Config file to use.",
)
@click.option("-d", "--dry", is_flag=True, help="Dry run, do not execute any commands.")
@click.pass_context
def robotcode(ctx: click.Context, config_file: Optional[Path], dry: Optional[bool] = None) -> None:
    """\b
 _____       _           _    _____          _
|  __ \\     | |         | |  / ____|        | |
| |__) |___ | |__   ___ | |_| |     ___   __| | ___
|  _  // _ \\| '_ \\ / _ \\| __| |    / _ \\ / _  |/ _ \\
| | \\ \\ (_) | |_) | (_) | |_| |___| (_) | (_| |  __/
|_|  \\_\\___/|_.__/ \\___/ \\__|\\_____\\___/ \\__,_|\\___|

"""
    ctx.ensure_object(dict)
    ctx.obj["config_file"] = config_file
    ctx.obj["dry"] = dry


for p in PluginManager().cli_commands:
    for c in p:
        robotcode.add_command(c)


@robotcode.command()
@click.pass_context
def debug(ctx: click.Context) -> None:
    """Debug the robotframework run."""
    click.echo("TODO")


@robotcode.command()
@click.pass_context
def clean(ctx: click.Context) -> None:
    """Clean the robotframework project."""
    click.echo("TODO")


@robotcode.command()
@click.pass_context
def new(ctx: click.Context) -> None:
    """Create a new robotframework project."""
    click.echo("TODO")
