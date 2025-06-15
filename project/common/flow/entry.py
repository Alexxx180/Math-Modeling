from common.commander.switch import are_defaults
from common.commander.resources import Resources

def AbstractRandomEntry(method, name: str) -> None:
	if are_defaults():
		args: list = Resources.Defaults[name]
	else:
		args: list = Resources.Input[name]()

	method(name, args)

def AbstractRandomEntryCMD(method, name: str) -> None:
	args: list = Resources.Defaults[name]
	return method(args, name)
