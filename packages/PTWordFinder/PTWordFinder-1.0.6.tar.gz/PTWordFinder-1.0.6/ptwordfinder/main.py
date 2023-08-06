""" Entrypoint of the CLI """
import click

from ptwordfinder.commands import calculate_words

@click.group()
def cli():
    pass


cli.add_command(calculate_words)