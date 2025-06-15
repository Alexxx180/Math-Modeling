from inquirer import prompt, Confirm, Text
from common.commander.resources import Resources

def __confirm(message: str) -> bool:
	name: str = 'confirm'
	return prompt([Confirm(name, message=message, default=True)])[name]

def _common(name: str) -> bool:
	return __confirm(Resources.Texts['Common'][name])

def are_defaults() -> bool: return _common('Defaults')
def swap_instead_repeat() -> bool: _common('Range')

def View(control: str, method: str) -> bool:
	on: bool = Resources.Enabled[control][method]
	return on or __confirm(Resources.Hints[control][method])
