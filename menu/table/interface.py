from common.commander.switch import View
from common.flow.texts.table import Text
from menu.table.solutions.solution import RandomDistribution

"""
This program takes a probability value table, generate random numbers.
Then calculate math expectation, dispersia, and evaluate both results
"""
def RandomTableReverseMethod(name: str, args: list) -> None:
    table = get_table(args)
    text = Text(name)
    text.table(table)
    text.research(table.math)

    if View('Table', name):
        text.source(table.matrix)

    text.pause()

def get_result(args: list) -> str:
    table = get_table(args)
    m: dict = table.m
    return " - ".join([m["expect"], m["dispersia"], str(table.matrix)])

def get_table(args: list):
    table = RandomDistribution(args)
    table.generate_random()
    table.output_first_quantity()
    return table
