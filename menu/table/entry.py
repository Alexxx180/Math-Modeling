from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.table.interface import RandomTableReverseMethod

def RandomTableEntry() -> None:
	name: str = 'table'

	if are_defaults():
		args: list = Resources.Defaults[name]
	else:
		args: list = Resources.Input[name]()

	RandomTableReverseMethod(name, args)
