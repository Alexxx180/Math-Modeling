from sympy.abc import x, r
from sympy import solve, lambdify, sqrt, N, Symbol, init_printing#, pprint
from common.calculus.trigonometry import form, invokation, express, integral, un_integral
from common.commander.resources import Resources

class RandomModel:
	def __init__(self, ab: tuple) -> None:
		self.f: str = Resources.Formula["continuous"]
		self.ab: tuple = ab
		self.POSITIVE: int = 1
		self.get_inverse().expectation().dispersia().evaluation().dis_evaluation()
		self.f = RandomModel.cute(self.f)

	def _get_inverse_sum(self) -> list:
		return solve(express(self.F) - r, x)

	def _get_inverse_mul(self) -> list:
		fInv = Symbol("f^-1")
		return solve(express(self.F) * fInv - 1, fInv)

	@staticmethod
	def cute(f: str) -> str:
		return f.replace("sqrt", "√").replace("exp", "e").replace("**", "`").replace("*", "⋅")

	def get_inverse(self):
		self.F = str(un_integral(express(self.f))) + str(self.ab[0] * (-1))
		#inverse: list = self._get_inverse_mul()
		inverse: list = self._get_inverse_sum()
		if len(inverse) > self.POSITIVE:
			self.inverse = inverse[self.POSITIVE]
		else:
			self.inverse = inverse[0]
		self.G = str(self.inverse).replace("x", "r")
		method = lambdify(r, express(self.G), "numpy")
		self.G = RandomModel.cute(self.G)
		self.F = RandomModel.cute(self.F)
#		self.F = 
		#init_printing()
		#pprint(express(self.G))
		self.method = lambda r: self.debug_m(r, method) #(method(r) + float(self.ab[0])) % float(self.ab[1])
		return self

	def debug_m(self, r, method):
		value: float = method(r)
		if self.ab[0] > 0:
			value = abs(value)
		value %= self.ab[1]
		if value < self.ab[0]:
			value += self.ab[0]
		return value

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
