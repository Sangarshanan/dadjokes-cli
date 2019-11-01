from dadjokes.sources import (
	get_wesbos_dad_jokes
	)

dad_jokes_complilation = []

def compile_dad_jokes():
	wesbos_dad_jokes_list = get_wesbos_dad_jokes()
	dad_jokes_complilation.extend(wesbos_dad_jokes_list)
	return dad_jokes_complilation