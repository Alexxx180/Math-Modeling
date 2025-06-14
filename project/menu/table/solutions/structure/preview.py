from common.commander.resources import Resources

def fill_values(self, row: dict, cell: int) -> None:
	count: int = min(row["q"], row["columns"])
	for column in range(count):
		i: int = self.i[cell + column]
		row["next"].append(row["x"][i])

def fill_blanks(row: dict) -> None:
	for i in range(len(row["next"]), row["columns"]):
		row["next"].append(Resources.Fields["table"]["selection"]["empty"])

def decide_x(math, row: dict) -> None:
	if hasattr(math, 'xf'):
		row["x"] = math.xf
	else:
		row["x"] = math.x

def _table_length(columns: int, q: int) -> int:
	length: int = int(q / columns)
	if q % columns != 0: length = length + 1
	return length

def _add_table_row(self, row: dict, no: int) -> None:
	row["next"] = []
	fill_values(self, row, no * row["columns"])
	fill_blanks(row)
	self.r.append(row["next"])
	row["q"] -= row["columns"]

def _get_table_columns() -> int:
	return max(len(Resources.Fields["table"]["selection"]["source"]) - 1, 1)

def get_preview(self, math) -> None:
	row: dict = { "columns": _get_table_columns(), "q": self.quantity }
	decide_x(math, row)
	length: int = _table_length(row["columns"], row["q"])

	for number in range(length):
		_add_table_row(self, row, number)
