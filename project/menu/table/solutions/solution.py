from menu.table.solutions.calculus import RandomCalculus
from menu.table.solutions.selection import RandomSelection
from menu.table.solutions.structure.lists import convert_to_list, enum_format
from menu.table.solutions.structure.methods import method_reverse

class RandomDistribution:
	def __init__(self, args: dict) -> None:
		if "ab" in args: self.ab = args["ab"]
		self.math = RandomCalculus(args["X"], args["p"])
		self.init = RandomSelection(args["N"], args["q"])
		self.method = self.reverse_method

	def to_list(self, name: str) -> list:
		return convert_to_list(self, name)

	def set_method(self, model) -> None:
		self.model = model
		self.method = model.method
		self.math.set_expecting(model.expecting)
		self.math.set_dispersing(model.dispersing)
		self.math.set_evaluating(model.evaluating)
		self.math.set_dis_evaluating(model.dis_evaluating)
		return self

	def reverse_method(self, value: float) -> float:
		return method_reverse(self, value) # % float(self.ab[1]) + self.ab[0]

	def generate_values(self, method) -> None:
		x: list = self.init.generate_values(method)
		self.math.x = x
		# self.math.xf = enum_format(x)

	def start(self):
		if len(self.math.x) == 0:
			self.generate_values(self.method)
		else:
			self.init.generate_random(self.method)
		self.init.calculate(self.math)
		return self
