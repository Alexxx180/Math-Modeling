from common.drawing.table.table import Table
from common.handlers.interaction import pause
from common.handlers.printer import Printer
from common.commander.resources import Resources

class Text:
	def __init__(self, name: str) -> None:
		self.fields: dict = Resources.Fields[name]
		self.p = Printer(name).act(print)

	def table(self, args):
		self.p.keys("Table").args(args).print()
		return self

	def formula(self, args):
		self.p.keys("Formula").args(args).print()
		return self

	@staticmethod
	def format_columns(fields) -> list:
		f1: list = fields["format"][1].copy()
		fa: list = fields["format"][0]
		for i in range(len(f1)):
			f1[i] = '%' + ".%df" % (fa[0] if fa[1] else f1[i])
		return f1

	def format_matrix(f: list, matrix) -> list:
		for i in range(len(f)):
			for row in matrix:
				if row[i] != '':
					row[i] = f[i] % row[i]

	def research(self, result: list):
		rows: list = []
		f: list = Text.format_columns(self.fields["initial"])
		for struct in result:
			i = struct.init
			m = struct.math
			rows.append([i.numbers, f[0] % m.m_expect, f[1] % m.m_eval, f[2] % m.delta[1],
				f[3] % m.dispersia, f[4] % m.ground, f[5] % m.delta[2]])
		Table(self.fields["initial"]["source"].copy()).rows(rows).show()
		return self

	def source(self, matrix):
		f: list = Text.format_columns(self.fields["selection"])
		Text.format_matrix(f, matrix)
		Table(self.fields["selection"]["source"].copy()).rows(matrix).show()
		return self

	def pause(self, text: str = '') -> None: pause(text)
