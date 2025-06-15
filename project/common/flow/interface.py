from common.commander.switch import View
from common.flow.texts.table import Text
from menu.table.solutions.solution import RandomDistribution

def get_table(args: list, struct):
	adapt: dict = struct.get_adapter(args)
	model = struct(adapt["ab"])
	return RandomDistribution(adapt).set_method(model).start()

def single_row(args, struct, N: int = 100):
	return [get_table([args[0], args[1], N, args[2]], struct)]

def double_row(args, struct):
	return [single_row(args, struct)[0], single_row(args, struct, 10000)[0]]

def raw_rows(args, _struct = None): return RandomDistribution(args).start()

def source_single(result): return result[0]
def source_whole(result): return result

def AbstractRandomMethod(name: str, args: list, _result, _text, _source, struct = None) -> None:
	result = _result(args, struct)
	text = _text(name, result)

	if View('Table', name):
		text.source(_source(result).init.r)

	text.pause()

def formuled(name, result):
	return Text(name).formula(result[0].model).table(result[0]).research(result)

def discrete(name, table):
	return Text(name).table(table).research([table])
