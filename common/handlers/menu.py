from common.handlers.interaction import ask
from menu.table.entry import RandomTableEntry

invoke: dict = {
    'table': RandomTableEntry,
}

def select(query: str, choices: dict, options: dict):
    answers = ask(options[query])
    for key, value in choices.items():
        if answers[query] == key:
            invoke[query](value)
