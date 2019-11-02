import click
import random
from cowpy import cow

from dadjokes.sources import (
	get_wesbos_dad_jokes,
	get_icanhazdadjoke,
	get_post_reddit
	)

@click.command()
@click.option('--cowsay',is_flag=True, help="Summon the Cowsay Characters")
@click.option('--icanhazdad',is_flag=True, help="Get jokes from icanhazdadjoke.com")
@click.option('--github',is_flag=True, help="Get jokes from github.com/wesbos/dad-jokes")
@click.option('--reddit',is_flag=True, help="Get DadJokes from Reddit")
def cli(cowsay,icanhazdad,github,reddit):
	if icanhazdad:
		dadjoke = random.choice(get_icanhazdadjoke())
	elif github:
		dadjoke = random.choice(get_wesbos_dad_jokes())
	elif reddit:
		dadjoke = random.choice(get_post_reddit('DadJokes'))
	else:
		dadjoke = random.choice(get_wesbos_dad_jokes())
	if cowsay:
		click.echo(cow.milk_random_cow(dadjoke))
	else:
		click.echo(dadjoke)