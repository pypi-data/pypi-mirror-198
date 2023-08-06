import json
from typing import Optional

from edgescan.api.client import Client
from edgescan.cli.helpers import str_to_strs, str_to_ints, str_to_datetime

import click
import itertools
import edgescan.serialization
import edgescan.tallies


@click.group()
def assets():
    """
    Query or count assets.
    """
    pass


@assets.command()
@click.option('--asset-id', type=int, required=True)
def get_asset(asset_id: int):
    """
    Lookup assets.
    """
    api = Client()
    row = api.get_asset(asset_id=asset_id)
    if row:
        txt = edgescan.serialization.to_json(row)
        click.echo(txt)


@assets.command()
@click.option('--asset-ids')
@click.option('--names')
@click.option('--tags')
@click.option('--min-create-time')
@click.option('--max-create-time')
@click.option('--min-update-time')
@click.option('--max-update-time')
@click.option('--limit', type=int)
def get_assets(
        asset_ids: Optional[str],
        names: Optional[str],
        tags: Optional[str],
        min_create_time: Optional[str],
        max_create_time: Optional[str],
        min_update_time: Optional[str],
        max_update_time: Optional[str],
        limit: Optional[int] = None):
    """
    Search for assets.
    """
    api = Client()
    rows = api.iter_assets(
        ids=str_to_ints(asset_ids),
        names=str_to_strs(names),
        tags=str_to_strs(tags),
        min_create_time=str_to_datetime(min_create_time),
        max_create_time=str_to_datetime(max_create_time),
        min_update_time=str_to_datetime(min_update_time),
        max_update_time=str_to_datetime(max_update_time),
    )
    for row in itertools.islice(rows, limit):
        txt = edgescan.serialization.to_json(row)
        click.echo(txt)


@assets.command()
@click.argument('path', required=True)
def export_assets(path: str):
    """
    Write assets to a file.
    """
    client = Client()
    client.export_assets(path=path)


@assets.command()
@click.option('--asset-ids')
@click.option('--names')
@click.option('--tags')
@click.option('--min-create-time')
@click.option('--max-create-time')
@click.option('--min-update-time')
@click.option('--max-update-time')
@click.option('--group-by')
@click.option('--sort-by-key/--sort-by-value', default=True)
def count_assets(
        asset_ids: Optional[str],
        names: Optional[str],
        tags: Optional[str],
        min_create_time: Optional[str],
        max_create_time: Optional[str],
        min_update_time: Optional[str],
        max_update_time: Optional[str],
        group_by: Optional[str],
        sort_by_key: bool):
    """
    Count assets.
    """
    api = Client()

    if group_by:
        rows = api.iter_assets(
            ids=str_to_ints(asset_ids),
            names=str_to_strs(names),
            tags=str_to_strs(tags),
            min_create_time=str_to_datetime(min_create_time),
            max_create_time=str_to_datetime(max_create_time),
            min_update_time=str_to_datetime(min_update_time),
            max_update_time=str_to_datetime(max_update_time),
        )
        tally = edgescan.tallies.tally_by(rows, group_by)
        if sort_by_key:
            tally = edgescan.tallies.sort_by_key(tally)
        else:
            tally = edgescan.tallies.sort_by_value(tally)
        result = edgescan.serialization.to_json(tally)
    else:
        result = api.count_assets(
            ids=str_to_ints(asset_ids),
            names=str_to_strs(names),
            tags=str_to_strs(tags),
            min_create_time=str_to_datetime(min_create_time),
            max_create_time=str_to_datetime(max_create_time),
            min_update_time=str_to_datetime(min_update_time),
            max_update_time=str_to_datetime(max_update_time),
        )
    
    print(result)

