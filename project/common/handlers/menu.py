from common.handlers.interaction import ask
from menu.table.entry import RandomTableEntry
from menu.model.entry import RandomModelEntry

invoke: dict = {
	'table': RandomTableEntry,
	'model': RandomModelEntry,
}

def select(query: str, choices: dict, options: dict):
	answers = ask(options[query])
	for key, value in choices.items():
		if answers[query] == key:
			invoke[query](value)
