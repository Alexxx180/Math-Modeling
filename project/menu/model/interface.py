from common.commander.switch import View
from common.flow.texts.table import Text
from menu.table.solutions.solution import RandomDistribution
from menu.model.solution import RandomModel

"""
This program takes a probability value table, generate random numbers.
Then calculate math expectation, dispersia, and evaluate both results
"""
def get_table(args: list):
	adapt: dict = RandomModel.get_adapter(args)
	model = RandomModel(adapt["ab"])
	return RandomDistribution(adapt).set_method(model).start()

def RandomModelReverseMethod(name: str, args: list) -> None:
	result = [get_table([args[0], args[1], 100, args[2]]),
		get_table([args[0], args[1], 10000, args[2]])]

	text = Text(name)
	text.formula(result[0].model).table(result[0]).research(result)

	if View('Table', name):
		text.source(result[0].init.r)

	text.pause()

def RandomModelReverseMethodCMD(args: list, name: str) -> str:
	return " - ".join(get_table(args).to_list(name))
