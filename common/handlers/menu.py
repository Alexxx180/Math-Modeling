from common.handlers.interaction import ask
from menu.rauss.entry import RaussEntry
from menu.hurwitz.entry import HurwitzEntry

invoke: dict = {
    'rauss': RaussEntry,
    'hurwitz': HurwitzEntry,
}

def select(query: str, choices: dict, options: dict):
    answers = ask(options[query])
    for key, value in choices.items():
        if answers[query] == key:
            invoke[query](value)
