from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.evenly.interface import RandomEvenlyMethod, RandomEvenlyMethodCMD

name: str = 'evenly'

def RandomEvenlyEntry() -> None:
	if are_defaults():
		args: list = Resources.Defaults[name]
	else:
		args: list = Resources.Input[name]()

	RandomEvenlyMethod(name, args)

def RandomEvenlyEntryCMD() -> None:
	args: list = Resources.Defaults[name]
	return RandomEvenlyMethodCMD(args, name)
