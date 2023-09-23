import click

from pbutil import module1
from pbutil.module2 import module2


@click.command()
@click.option("--arg", type=str)
def cli(arg: str) -> None:
    print(module2.that_function(module1.some_function(arg)))
