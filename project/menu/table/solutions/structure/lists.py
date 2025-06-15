from common.commander.resources import Resources

def form(numbers: int, value) -> str: # "{0:.3f}"
	fr: str = ('%' + ".%df" % numbers)
#	print("VALUE: ", value)
	return ('%' + ".%df" % numbers) % value

def enum_format(n: int, value: list) -> list:
	# return [v for v in value]
	return [('""' if v == '' else (form(n, v).replace("'", ""))) for v in value]

def _list_to_str(value: list, n: int, skip_format: bool) -> str:
	result: str = str(value) if skip_format else str(enum_format(n, value))
	return result.replace("[", "").replace("]", "").replace("'", "").replace('"', "'")
#			   .replace("'\d+", "")

def convert_to_list(struct, name: str) -> list:
	skip: bool = False
	f: dict = Resources.Fields["format"]
	result: list = struct.math.to_list(name)
	result.append(str(struct.init.numbers))
	result.append(str(struct.init.quantity))
	result.append(_list_to_str(struct.math.x, f["X"], skip))

	if len(struct.math.p) > 0:
		result.append(_list_to_str(struct.math.p, f["p"], skip))

	r: list = []
	for row in struct.init.r:
		r.append(_list_to_str(row, f["q"], skip))

	result.append(" + ".join(r))
	return result

