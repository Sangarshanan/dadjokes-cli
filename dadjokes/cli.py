import click
import random
from cowpy import cow

from dadjokes.main import compile_dad_jokes
from dadjokes.cowsay_characters import (
	COW
	)

@click.command()
@click.option('--cowsay',is_flag=True, help="Summon the Cowsay Characters")
def cli(cowsay):
	dad_jokes = compile_dad_jokes()
	dadjoke = random.choice(dad_jokes)
	if not cowsay:
		click.echo(dadjoke)
	else:
		
		click.echo(cow.milk_random_cow(dadjoke))