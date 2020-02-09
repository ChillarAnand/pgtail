### pgtail

Tail your postgres table inserts like a file.


### Installation

    $ pip install pgtail


### Usage

To tail a table, run

    $ pgtail postgres://user:pass@localhost:5432/database table

By default, it will tail from the last row of the table.

To tail last 10 rows, every 5 seconds, run

    $ pgtail postgres://user:pass@localhost:5432/database table 10 5

To see help, run

    $ pgtail --help
