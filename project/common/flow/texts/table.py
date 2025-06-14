from common.drawing.table.table import Table
from common.handlers.interaction import pause
from common.handlers.printer import Printer
from common.commander.resources import Resources

class Text:
	def __init__(self, name: str) -> None:
		self.fields: dict = Resources.Fields[name]
		self.p = Printer(name).act(print)

	def table(self, args) -> None:
		self.p.keys("Table").args(args).print()
		return self

	def formula(self, args) -> None:
		self.p.keys("Formula").args(args).print()
		return self

	def research(self, result: list) -> None:
		f: str = "%.4f"
		rows: list = []
		for struct in result:
			i = struct.init
			m = struct.math
			rows.append([i.numbers, f % m.m_expect, f % m.m_eval, f % m.delta[1], f % m.dispersia, f % m.ground, f % m.delta[2]])
		Table(self.fields["initial"]["source"].copy()).floats("0.4f").rows(rows).show()
		return self

	def source(self, matrix) -> None:
		Table(self.fields["selection"]["source"].copy()).rows(matrix).show()
		return self

	def pause(self, text: str = '') -> None:
		pause(text)
