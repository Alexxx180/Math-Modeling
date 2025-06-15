# from sympy.abc import x, r
# from sympy import solve, lambdify, sqrt, N, Symbol
# from common.calculus.trigonometry import form, invokation, express, integral, un_integral
# from common.commander.resources import Resources

class RandomEvenly:
	def __init__(self, ab: tuple) -> None:
		self.fx: str = "a + rᵢ(b - a)"
		self.fm: str = "(a + b) / 2"
		self.fd: str = "(b - a²) / 12"
		self.ab: tuple = ab
		self.POSITIVE: int = 1
		self.get_method().expectation().dispersia()

	def get_method(self):
		self.method = lambda r: self.ab[0] + r * (self.ab[1] - self.ab[0])
		# % self.ab[1] + self.ab[0]
		return self

	def expectation(self) -> None:
		self.expecting = lambda: (self.ab[0] + self.ab[1]) / 2
		return self

	def dispersia(self) -> None:
		self.dispersing = lambda e: (self.ab[0] + self.ab[1] ** 2) / 12
		return self

	@staticmethod
	def get_adapter(args: list) -> dict:
		ab: tuple = (args[0], args[1])
		return { "ab": ab, "N" : args[2], "q" : args[3], "X" : [], "p" : [] }
