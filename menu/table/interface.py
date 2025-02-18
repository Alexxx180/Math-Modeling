from common.commander.switch import View
from common.flow.texts.table import Text
from menu.table.solutions.solution import RandomDistribution

"""
This program takes a probability value table, generate random numbers.
Then calculate math expectation, dispersia, and evaluate both results
"""
def RandomTableReverseMethod(name: str, args: dict) -> None:
	table = RandomDistribution(args).start()
	text = Text(name).table(table).research(table.math)

	if View('Table', name):
		text.source(table.init.r)

	text.pause()

def get_result(args: dict) -> str:
	return " - ".join(RandomDistribution(args).start().to_list())
