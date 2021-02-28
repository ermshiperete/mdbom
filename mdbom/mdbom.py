"""Main module for the MdBOM CLI tool.

MdBOM takes a CycloneDX standard bom.json
file and extracts relevant data from it for
creating a 3rd party software markdown document.
"""

import logging

import click

log_handler = logging.StreamHandler()
log_handler.setLevel(logging.INFO)
log_formatter = logging.Formatter("%(levelname)s [%(module)s] : %(message)s")
log_handler.setFormatter(log_formatter)

logging.basicConfig(level=logging.NOTSET, handlers=[log_handler])

logger = logging.getLogger("MdBOM")


@click.group()
def cli():
    """Run the main entry point for MdBOM."""
    pass


@click.command()
def info():
    """Print a simple info about MdBOM."""
    click.echo("Check the documentation: https://haro87.github.io/mdbom/")
    click.echo("for further information.")


cli.add_command(info)
