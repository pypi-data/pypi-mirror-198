# coding: utf-8

import click


@click.group()
def cli():
    """BonnieTools - Command line tool for Bonnie"""
    pass


@cli.command()
def excel():
    print('go')
