import logging
import sys
from pathlib import Path
from typing import Optional

import click

from . import __version__
from .data_models import Configuration

logger = logging.getLogger("DukeTypem2D")


def config_logger(verbose: int) -> None:
    # calc logging level: debug (10) up to error (40)
    verbose = 10 * (4 - min(max(verbose, 0), 4))
    logger.setLevel(verbose)  # 10

    logging.basicConfig(format="%(message)s")  # reduce internals


@click.group(context_settings={"help_option_names": ["-h", "--help"], "obj": {}})
@click.option(
    "-v",
    "--verbose",
    count=True,
    default=0,
    help="4 Levels [0..3](Error, Warning, Info, Debug)",
)
@click.pass_context
def cli(ctx: click.Context, verbose: int) -> None:
    """Duke Typem 2D: Improve readability, spelling and expression of your text documents"""
    config_logger(verbose)
    logger.info("Program v%s", __version__)
    logger.debug("Python  v%s", sys.version)
    logger.debug("Click   v%s\n", click.__version__)
    if not ctx.invoked_subcommand:
        click.echo("Please specify a valid command")


@cli.command(short_help="Analyze text-files")
@click.argument(
    "in_data",
    type=click.Path(exists=True, resolve_path=False, file_okay=True, dir_okay=True),
    required=False,
)
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=False),
    default=None,
    help="user-provided config (YAML or TOML)",
)
def check(in_data: Path, config: Optional[Path]) -> None:
    """
    TODO:
    - distinguish between path and file
    - strip, analyze, fix ... separate src-file
    """
    found_problem = False
    _cfg = Configuration.parse_file(config)
    if in_data is not None:
        data = Path(in_data)
        if data.exists():
            _cfg.project_path = str(data)
        else:
            raise ValueError("Provided path must exist (='%s')", data)

    sys.exit(int(found_problem))


@cli.command(short_help="Create example config")
@click.argument(
    "out_path",
    type=click.Path(file_okay=True, dir_okay=False, resolve_path=False, exists=False),
    default=Path("./.DukeTypem2D"),
)
@click.option(
    "--style",
    "-s",
    type=click.Choice(["yaml", "toml"]),
    default="yaml",
    help="Choose your flavor",
)
def init(out_path: Path, style: str) -> None:
    config = Configuration()
    config.to_file(out_path, style=style, version=__version__)


if __name__ == "__main__":
    logger.info("This File should not be executed like this ...")
    cli()
