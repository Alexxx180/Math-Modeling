from inquirer import prompt
from common.commander.resources import Resources

def verify(request: callable, default) -> bool:
    try:
        value = request()
        return (True, value)
    except ValueError:
        return (False, default)

def validate(request: callable) -> bool:
    try:
        request()
        return True
    except ValueError:
        return False

def specify(convert: callable, check: callable, arg: tuple, error: str, *conditions):
    query: callable = lambda: convert(prompt(Resources.Queries[arg[0]])[arg[0]])
    parameter: tuple = verify(query, arg[1])
    while not parameter[0] or check(parameter[1]):
        errors.keys(error).args(conditions).print()
        parameter = verify(query, arg[1])
    return parameter[1]

def number(_, response) -> bool:
    valid: bool = validate(lambda: float(response))
    if not valid: print(Resources.Texts['Common']['Invalid'])
    return valid

def list_argument(parameters: list, convert: callable, arg: str) -> bool:
    if arg == '':
        parameters.append(convert(0))
        return True

    query = Resources.Queries[arg]
    request: callable = lambda: parameters.append(convert(prompt(query)[arg]))

    return validate(request)
