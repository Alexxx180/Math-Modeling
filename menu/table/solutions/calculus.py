from typing import Callable

class RandomCalculus:
	def __init__(self, x: list, p: list) -> None:
		self.eval: float = 0      # m - math evaluation
		self.ground: float = 0    # g - dispersia evaluation
		self.expect: float = 0    # M - math expectation
		self.dispersia: float = 0 # D - dispersia
		self.x: list = x          # [4, -7, 6]
		self.p: list = p          # [0.1, 0.5, 0.4] # probability

	def is_one_probability(self, segment: float) -> None:
		assert((segment == 1), "Sum probability must be 1.")

	def check_count(self, numbers: int, count: int) -> None:
		for i in range(count):
			assert((numbers - i == 0), "Too short data - zero division.")

	def expectation(self, k: int) -> None: # Σ(xₖpₖ)
		self.expect += self.x[k] * self.p[k]

	def get_dispersia(self, k: int) -> None: # Σ(pₖ(xₖ - M)²)
		self.dispersia += self.p[k] * (self.x[k] - self.expect) ** 2

	def evaluation(self, k: int) -> None: # Σ(xₖ)
		self.eval += self.x[k]

	def evaluation_end(self, n: int) -> None: # m / N
		self.eval /= n

	def dispersia_ground(self, k: int) -> None: # Σ(xₖ²)
		self.ground += self.x[k] ** 2

	# g / N - 1 - (N / N - 1)m²
	def dispersia_ground_end(self, n: int) -> None:
		self.ground /= n - 1
		self.ground -= (n / n - 1) * (self.eval ** 2)
