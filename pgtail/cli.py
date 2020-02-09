import time
from pprint import pprint

import click
import psycopg2


def fetch_data(cursor, table, rows):
    query = '''
    SELECT * FROM {}
    ORDER BY id DESC
    LIMIT {};
    '''.format(table, rows)
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def pgtail(db, table, rows, interval):
    connection = psycopg2.connect(dsn=db)
    cursor = connection.cursor()
    previous = None
    while True:
        current = fetch_data(cursor, table, rows)
        if current != previous:
            pprint(current)
            previous = current
        time.sleep(interval)


@click.command()
@click.argument('db', required=True)
@click.argument('table', required=True)
@click.argument('rows', default=1, required=False)
@click.argument('interval', default=1, required=False)
def main(db, table, rows, interval):
    """pgtail"""
    click.echo('pgtail: db {} - table {} - rows {} - interval {}s'.format(db, table, rows, interval))
    pgtail(db, table, rows, interval)
