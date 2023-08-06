from typing import Optional
from edgescan.api.client import Client

import itertools
import click

import edgescan.tallies
import edgescan.serialization
from edgescan.cli.helpers import str_to_strs, str_to_ints


@click.group()
def licenses():
    """
    Query or count licenses.
    """
    pass


@licenses.command()
@click.option('--license-id', type=int, required=True)
def get_license(license_id: int):
    """
    Lookup licenses by ID.
    """
    api = Client()
    row = api.get_license(license_id)
    if row:
        txt = edgescan.serialization.to_json(row)
        click.echo(txt)


@licenses.command()
@click.option('--license-ids')
@click.option('--license-names')
@click.option('--expired/--not-expired', default=None)
@click.option('--limit', type=int)
def get_licenses(
        license_ids: Optional[str],
        license_names: Optional[str],
        expired: Optional[bool],
        limit: Optional[int]):
    """
    List licenses.
    """
    api = Client()
    rows = api.iter_licenses(
        ids=str_to_ints(license_ids),
        names=str_to_strs(license_names),
        expired=expired,
    )
    for row in itertools.islice(rows, limit):
        txt = edgescan.serialization.to_json(row)
        click.echo(txt)


@licenses.command()
@click.argument('path', required=True)
def export_licenses(path: str):
    """
    Write licenses to a file.
    """
    client = Client()
    client.export_licenses(path=path)


@licenses.command()
@click.option('--license-ids')
@click.option('--license-names')
@click.option('--expired/--not-expired', default=None, show_default=True)
@click.option('--group-by')
@click.option('--sort-by-key/--sort-by-value', default=True)
def count_licenses(
    license_ids: Optional[str], 
    license_names: Optional[str], 
    expired: Optional[bool],
    group_by: Optional[str],
    sort_by_key: bool):
    """
    Count licenses.
    """
    api = Client()

    if group_by:
        rows = api.iter_licenses(
            ids=str_to_ints(license_ids),
            names=str_to_strs(license_names),
            expired=expired,
        )
        tally = edgescan.tallies.tally_by(rows, group_by)
        if sort_by_key:
            tally = edgescan.tallies.sort_by_key(tally)
        else:
            tally = edgescan.tallies.sort_by_value(tally)
        result = edgescan.serialization.to_json(tally)
    else:
        result = api.count_licenses(
            ids=str_to_ints(license_ids),
            names=str_to_strs(license_names),
            expired=expired,
        )
    print(result)
