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

	def research(self, initial) -> None:
		self.p.keys('Research').args(initial).print()
		return self

	def source(self, matrix) -> None:
		Table(self.fields["Source"].copy()).rows(matrix).show()
		return self

	def pause(self, text: str = '') -> None:
		pause(text)
