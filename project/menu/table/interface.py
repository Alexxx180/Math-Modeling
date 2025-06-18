from common.flow.interface import AbstractRandomMethod, get_table, single_row, double_row, triple_row, raw_rows, source_single, source_whole, formuled, discrete
from menu.evenly.solution import RandomEvenly
from menu.table.solutions.solution import RandomDistribution

"""
This program takes a probability value table, generate random numbers.
Then calculate math expectation, dispersia, and evaluate both results
"""
def RandomTableReverseMethod(name: str, args: dict) -> None:
	AbstractRandomMethod(name, args, double_row, discrete, source_single)

def RandomTableReverseMethodCMD(args: dict, name: str) -> str:
#	return " - ".join(raw_rows(args).to_list(name))
	return " - ".join(RandomDistribution(args).start().to_list(name))
