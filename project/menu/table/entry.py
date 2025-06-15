from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.table.interface import RandomTableReverseMethod, RandomTableReverseMethodCMD

name: str = 'table'

def RandomTableEntry() -> None:
	if are_defaults():
		args: list = Resources.Defaults[name]
	else:
		args: list = Resources.Input[name]()

	RandomTableReverseMethod(name, args)

def RandomTableEntryCMD() -> str:
	args: list = Resources.Defaults[name]
	return RandomTableReverseMethodCMD(args, name)
