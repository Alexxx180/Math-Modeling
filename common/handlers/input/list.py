from common.commander.resources import Resources
from common.handlers.interaction import pause
from common.handlers.input.validate import list_argument

def __pass_argument(parameters: list, convert: callable, args):
    if isinstance(args, str):
        list_argument(parameters, convert, args)
        return

    for name in args:
        while not list_argument(parameters, convert, name):
            pause(f"{Resources.Texts['Common']['Invalid']}\n")

def __specific_argument(parameters: list, validator: callable):
    args = validator()
    if isinstance(args, tuple):
        parameters.extend(args)
    else:
        parameters.append(args)

def listing(*args):
    parameters: list = []

    for arg in args:
        if isinstance(arg, tuple) and len(arg) == 2:
            __pass_argument(parameters, arg[0], arg[1])
        else:
            __specific_argument(parameters, arg)

    return parameters
