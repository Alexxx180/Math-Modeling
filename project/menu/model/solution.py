from sympy.abc import x, r
from sympy import solve, lambdify, sqrt, N, Symbol
from common.calculus.trigonometry import form, invokation, express, integral, un_integral
from common.commander.resources import Resources

class RandomModel:
	def __init__(self, ab: tuple) -> None:
		self.f: str = Resources.Formula["continuous"]
		self.ab: tuple = ab
		self.POSITIVE: int = 1
		self.get_inverse().expectation().dispersia().evaluation().dis_evaluation()

	def _get_inverse_sum(self) -> list:
		return solve(express(self.F) - r, x)

	def _get_inverse_mul(self) -> list:
		fInv = Symbol("f^-1")
		return solve(express(self.F) * fInv - 1, fInv)

	def get_inverse(self):
		self.F = str(un_integral(express(self.f)))
		inverse: list = self._get_inverse_mul()
		if len(inverse) > self.POSITIVE:
			self.inverse = inverse[self.POSITIVE]
		else:
			self.inverse = inverse[0]
		self.G = str(self.inverse).replace("x", "r")
		method = lambdify(r, express(self.G), "numpy")
		self.method = lambda r: method(r) % self.ab[1] + self.ab[0]
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

	def evaluation(self) -> None:
		self.evaluating = None
		return self

	def dis_evaluation(self) -> None:
		self.dis_evaluating = None
		return self

	@staticmethod
	def get_adapter(args: list) -> dict:
		ab: tuple = (args[0], args[1])
		return { "ab": ab, "N" : args[2], "q" : args[3], "X" : [], "p" : [] }
