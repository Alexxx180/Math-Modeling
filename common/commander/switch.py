from inquirer import prompt, Confirm, Text
from common.commander.resources import Resources

def __confirm(name: str, message: str) -> bool:
    return prompt([Confirm(name, message=message, default=True)])[name]

def are_defaults() -> bool:
    return __confirm('confirm', Resources.Texts['Common']['Defaults'])

def swap_instead_repeat() -> bool:
    return __confirm('confirm', Resources.Texts['Common']['Range'])

def View(control: str, method: str) -> bool:
    return Resources.Enabled[control][method] or __confirm(
        'confirm', Resources.Hints[control][method])
