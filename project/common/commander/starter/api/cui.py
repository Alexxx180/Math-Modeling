from inquirer import List
from common.handlers.platforms import clear
from common.handlers.interaction import ask
from common.handlers.menu import select, invoke
from common.commander.resources import Resources

def determine_option(answers: dict, key, value) -> None:
	if answers['option'] == key:
		if isinstance(value, list):
			select(value[0], value[1], Resources.Options)
		else:
			invoke[value]()

def set_options(answers: dict) -> dict:
	for key, value in Resources.Methods.items():
		determine_option(answers, key, value)
	return _query_user()

def _query_user() -> dict:
	clear()
	return ask(Resources.Main)

def dropdown() -> None:
	common: dict = Resources.Texts['Common']
	answers: dict = _query_user()
	while answers['option'] != common['Exit']:
		answers = set_options(answers)
	print(common['Finished'])

def choice(name: str) -> dict:
	return Resources.at('resources/switch/choices/' + name + '.json')

def _selection(method, options: dict, choices) -> list:
	return [List(method, message=options['message'], choices=choices)]

def setup_options() -> None:
	options: dict = choice('options')
	for method, choices in options['choices'].items():
		Resources.Options[method] = _selection(method, options, choices)

def setup_menu() -> None:
	main: dict = choice('main')
	Resources.Main = _selection('option', main, main['choices'])
	Resources.Methods = choice('methods')
	# setup_options()
