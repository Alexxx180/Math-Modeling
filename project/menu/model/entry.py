from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.model.interface import RandomModelReverseMethod

def RandomModelEntry() -> None:
	name: str = 'continuous'

	if are_defaults():
		args: list = Resources.Defaults[name]
	else:
		args: list = Resources.Input[name]()

	RandomModelReverseMethod(name, args)
