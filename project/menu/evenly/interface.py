from common.flow.interface import AbstractRandomMethod, get_table, single_row, double_row, triple_row, raw_rows, source_single, source_whole, formuled, discrete
from menu.evenly.solution import RandomEvenly

"""
This program generate random numbers by inner formula.
"""
def RandomEvenlyMethod(name: str, args: list) -> None:
	AbstractRandomMethod(name, args, single_row, formuled, source_single, RandomEvenly)

def RandomEvenlyMethodCMD(args: list, name: str) -> str:
	return " - ".join(get_table(args, RandomEvenly).to_list(name))
