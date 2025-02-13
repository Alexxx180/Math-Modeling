from common.commander.switch import View
from common.flow.texts.table import Text
from menu.table.solutions.solution import RandomDistribution

"""
This program takes a probability value table, generate random numbers.
Then calculate math expectation, dispersia, and evaluate both results
"""
def RandomTableReverseMethod(name: str, args: list) -> None:
	table = RandomDistribution(args).start()
	text = Text(name)
	text.table(table)
	text.research(table.math)

	if View('Table', name):
		text.source(table.init.r)

	text.pause()

def get_result(args: list) -> str:
	table = RandomDistribution(args).start()
	math = table.math
	init = table.init
	result: list = [math.expect, math.dispersia, math.eval, math.ground]
	result.extend([init.numbers, init.quantity, str(math.x), str(math.p), str(init.r)])
	return " - ".join(result)
