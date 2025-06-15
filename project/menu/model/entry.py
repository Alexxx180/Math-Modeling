from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.model.interface import RandomModelReverseMethod, RandomModelReverseMethodCMD

name: str = 'continuous'

def RandomModelEntry() -> None:
	if are_defaults():
		args: list = Resources.Defaults[name]
	else:
		args: list = Resources.Input[name]()

	RandomModelReverseMethod(name, args)

def RandomModelEntryCMD() -> None:
	args: list = Resources.Defaults[name]
	return RandomModelReverseMethodCMD(args, name)
