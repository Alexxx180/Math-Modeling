from inquirer import List
from platforms.cross import clear
from common.handlers.interaction import ask
from common.handlers.menu import select, invoke
from common.commander.resources import Resources

option: str = 'option'

def dropdown():
    clear()
    answers = ask(Resources.Main)
    while answers[option] != Resources.Texts['Common']['Exit']:
        for key, value in Resources.Methods.items():
            if answers[option] == key:
                if isinstance(value, list):
                    select(value[0], value[1], Resources.Options)
                else:
                    invoke[value]()
        clear()
        answers = ask(Resources.Main)
    print(Resources.Texts['Common']['Finished'])

def setup_options()
    options: dict = Resources.at('resources/switch/choices/options.json')
    for method, choices in options['choices'].items():
        Resources.Options[method] = [List(method, message=options['message'], choices=choices)]

def setup_menu():
    main: dict = Resources.at('resources/switch/choices/main.json')

    Resources.Main = [List(option, message=main['message'], choices=main['choices'])]
    Resources.Methods = Resources.at('resources/switch/choices/methods.json')

    # setup_options()
