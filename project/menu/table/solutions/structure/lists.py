def form(value) -> str:
	return "{0:.3f}".format(value)

def enum_format(value: list) -> list:
	return [form(v) for v in value]

def _list_to_str(value: list, skip_format: bool = False) -> str:
	result: str = str(value) if skip_format else str(enum_format(value))
	return result.replace("[", "").replace("]", "")

def convert_to_list(struct) -> list:
	skip: bool = True
	result: list = struct.math.to_list()
	result.append(str(struct.init.numbers))
	result.append(str(struct.init.quantity))
	result.append(_list_to_str(struct.math.x, skip))

	if len(struct.math.p) > 0:
		result.append(_list_to_str(struct.math.p, skip))

	r: list = []
	for row in struct.init.r:
		r.append(_list_to_str(row, skip))

	result.append(" + ".join(r))
	return result

