from common.commander.switch import View
from common.flow.texts.table import Text
from menu.table.solutions import RandomDistribution

def get_table(args: list) -> RandomDistribution:
    table = RandomDistribution(args)
    table.generate_random()
    table.output_first_quantity()
    table.math_evaluation()
    table.dispersia_ground()
    return table

"""
This program takes a probability value table and calculate
math expectation, dispersia, evaluation and ground ispersia
"""
def RandomTableReverseMethod(name: str, args: list) -> None:
    table = get_table(args)
    text = Text(name)
    text.table([table.numbers, table.quantity, [table.x, table.p]])
    text.research(table.m)

    if View('Table', name):
        text.source(table.matrix)

    text.pause()

def get_result(args: list) -> str:
    table = get_table(args)
    m: dict = table.m
    return " - ".join([m["expect"], m["dispersia"], str(table.matrix)])
