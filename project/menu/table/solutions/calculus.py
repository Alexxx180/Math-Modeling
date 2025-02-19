from typing import Callable

class RandomCalculus:
	def __init__(self, x: list, p: list) -> None:
		self.expecting = None     # expectation lambda
		self.dispersing = None    # dispersia lambda
		self.eval: float = 0      # m - math evaluation
		self.ground: float = 0    # g - dispersia evaluation
		self.expect: float = 0    # M - math expectation
		self.dispersia: float = 0 # D - dispersia
		self.x: list = x          # [4, -7, 6]
		self.p: list = p          # [0.1, 0.5, 0.4] # probability

	def to_list(self) -> list:
		return [self.expect, self.dispersia, self.eval, self.ground]

	def set_expecting(self, method) -> None:
		self.expecting = method

	def set_dispersing(self, method) -> None:
		self.dispersing = method

	def is_one_probability(self, segment: float) -> None:
		assert((segment == 1), "Sum probability must be 1.")

	def expectation(self, k: int) -> None: # Σ(xₖpₖ)
		self.expect += self.x[k] * self.p[k]

	def get_dispersia(self, k: int) -> None: # Σ(pₖ(xₖ - M)²)
		self.dispersia += self.p[k] * (self.x[k] - self.expect) ** 2

	def evaluation(self, k: int) -> None: # Σ(xₖ)
		self.eval += self.x[k]

	def evaluation_end(self, n: int) -> None: # m / N
		self.eval /= 1 if n == 0 else n

	def dispersia_ground(self, k: int) -> None: # Σ(xₖ²)
		self.ground += self.x[k] ** 2

	# g / N - 1 - (N / N - 1)m²
	def dispersia_ground_end(self, n: int) -> None:
		n1: int = n - 1 if n - 1 == 0 else 1
		self.ground /= n1
		self.ground -= (n / n1) * (self.eval ** 2)
