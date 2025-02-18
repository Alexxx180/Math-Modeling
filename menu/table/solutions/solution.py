from menu.table.solutions.calculus import RandomCalculus
from menu.table.solutions.selection import RandomSelection

class RandomDistribution:
	def __init__(self, args: dict) -> None:
		self.math = RandomCalculus(args["X"], args["p"])
		self.init = RandomSelection(args["N"], args["q"])
		self.method = self.reverse_method

	def to_list() -> list:
		result: list = math.to_list()
		result.extend([self.init.numbers, self.init.quantity])
		result.append(str(self.math.x))
		if len(self.math.p) > 0:
			result.append(str(self.math.p))
		result.append(str(self.init.r))
		return result

	def set_method(self, model) -> None:
		self.method = model.method
		self.math.set_expecting(model.expecting)
		self.math.set_dispersing(model.dispersing)
		return self

	def reverse_method(self, value: float) -> float:
		i: int = len(self.math.p)
		segment: float = sum(self.math.p)
		found: bool = value == segment
		self.math.is_one_probability(segment)

		while i > 0 and not found:
			i -= 1
			current: float = segment - self.math.p[i]
			found = value >= current and value < segment
			segment = current

		return i

	def sigma(self, formula) -> None: # Σ
		for j in range(self.numbers): formula(self.i[j])

	def start(self):
		if len(self.math.x) == 0:
			x: list = self.init.generate_values(self.method)
			self.math.x = x
			self.math.xf = ["{0:.3}".format(s) for s in x]
		else:
			self.init.generate_random(self.method)
		self.init.calculate(self.math)
		return self
