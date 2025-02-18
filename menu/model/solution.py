from sympy.abc import x, r
from sympy import solve, lambdify, sqrt, N
from common.calculus.trigonometry import form, invokation, express, integral
from common.commander.resources import Resources

class RandomModel:
	def __init__(self, ab: tuple) -> None:
		self.f: str = Resources.Formula["continuous"]
		self.ab: tuple = ab
		self.POSITIVE: int = 1
		self.get_inverse().expectation().dispersia()

	def get_inverse(self):
		self.inverse = solve(express(self.f) - r, x)
		if len(self.inverse) > 1:
			self.inverse = self.inverse[self.POSITIVE]
		self.G = str(self.inverse)
		self.method = lambdify(r, express(self.G), "numpy")
		return self

	def expectation(self) -> None:
		formula: str = "x * (%s)" % self.f
		self.e = integral(express(formula), self.ab)
		self.expecting = lambda: N(self.e)
		return self

	def dispersia(self) -> None:
		formula: str = "(x ** 2) * (%s)" % self.f
		self.d = integral(express(formula), self.ab)
		self.dispersing = lambda e: N(self.d - e ** 2)
		return self

	@staticmethod
	def get_adapter(args: list) -> dict:
		ab: tuple = (args[0], args[1])
		return { "ab": ab, "N" : args[2], "q" : args[3], "X" : [], "p" : [] }
