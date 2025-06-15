from common.flow.texts.table import Text
from common.commander.resources import Resources

def form(numbers: int, value) -> str:
	fr: str = ('%' + ".%df" % numbers)
	return ('%' + ".%df" % numbers) % value

def enum_format(n: int, value: list) -> list:
	return [('""' if v == '' else (form(n, v).replace("'", ""))) for v in value]

def _list_to_str(value: list, n: int = -1) -> str:
	result: str = str(value)
	if n != -1:
		result = str(enum_format(n, value))
	else:
		result = result.replace("''", "E")
	return result.replace("[", "").replace("]", "").replace("'", "").replace('E', "''")

def convert_to_list(struct, name: str) -> list:
	f: dict = Resources.Fields[name]["initial"]
	result: list = struct.math.to_list(name)
	result.append(str(struct.init.numbers))
	result.append(str(struct.init.quantity))
	result.append(_list_to_str(struct.math.x, f["X"]))

	if len(struct.math.p) > 0:
		result.append(_list_to_str(struct.math.p, f["p"]))

	f: dict = Text.format_columns(Resources.Fields[name]["selection"])
	Text.format_matrix(f, struct.init.r)

	r: list = []
	for row in struct.init.r:
		r.append(_list_to_str(row))

	result.append(" + ".join(r))
	return result

