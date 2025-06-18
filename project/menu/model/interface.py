from common.flow.interface import AbstractRandomMethod, get_table, single_row, double_row, triple_row, raw_rows, source_single, source_whole, formuled, discrete
from menu.model.solution import RandomModel

"""
This program takes a probability value table, generate random numbers.
Then calculate math expectation, dispersia, and evaluate both results
"""
def RandomModelReverseMethod(name: str, args: list) -> None:
	AbstractRandomMethod(name, args, double_row, formuled, source_single, RandomModel)

def RandomModelReverseMethodCMD(args: list, name: str) -> str:
	return " - ".join(get_table(args, RandomModel).to_list(name))
