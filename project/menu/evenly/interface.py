from common.commander.switch import View
from common.flow.texts.table import Text
from menu.table.solutions.solution import RandomDistribution
from menu.evenly.solution import RandomEvenly

"""
This program generate random numbers by inner formula.
"""
def get_table(args: list):
	adapt: dict = RandomEvenly.get_adapter(args)
	model = RandomEvenly(adapt["ab"])
	return RandomDistribution(adapt).set_method(model).start()

def RandomEvenlyMethod(name: str, args: list) -> None:
	result = [get_table([args[0], args[1], 100, args[2]])]
#    , get_table([args[0], args[1], 10000, args[2]])]

	text = Text(name)
	text.formula(result[0].model).table(result[0]).research(result)

	if View('Table', name):
		text.source(result[0].init.r)

	text.pause()

def RandomEvenlyMethodCMD(args: list) -> str:
	return " - ".join(get_table(args).to_list())
