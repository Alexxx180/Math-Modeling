from common.commander.switch import View
from common.flow.texts.table import Text
from menu.table.solutions.solution import RandomDistribution
from menu.model.solution import RandomModel

"""
This program takes a probability value table, generate random numbers.
Then calculate math expectation, dispersia, and evaluate both results
"""
def RandomModelReverseMethod(name: str, args: list) -> None:
	adapt: dict = RandomModel.get_adapter(args)
	model = RandomModel(adapt["ab"])
	table = RandomDistribution(adapt).set_method(model).start()

	text = Text(name)
	text.formula(model).table(table).research(table.math)

	if View('Table', name):
		text.source(table.init.r)

	text.pause()

def get_result(args: list) -> str:
	adapt: dict = RandomModel.get_adapter(args)
	model = RandomModel(adapt["ab"])
	table = RandomDistribution(adapt).set_method(model)
	return " - ".join(table.start().to_list())
