from typing import Callable
from common.commander.resources import Resources
from common.flow.texts.table import Text

class RandomCalculus:
	def __init__(self, x: list, p: list) -> None:
		# expectation evaluation lambda
		# self.evaluating = None
		self.evaluating = lambda s, m: RandomCalculus.table_eval(s, m)
		# dispersia evaluation lambda
		# self.dis_evaluating = None
		self.dis_evaluating = lambda s, m: RandomCalculus.table_diseval(s, m)
		self.expecting = None	 	# expectation lambda
		self.dispersing = None		# dispersia lambda
		self.m_eval: float = 0		# m - math evaluation
		self.ground: float = 0		# g - dispersia evaluation
		self.m_expect: float = 0	# M - math expectation
		self.dispersia: float = 0	# D - dispersia
		self.x: list = x			# [4, -7, 6]
		self.p: list = p			# [0.1, 0.5, 0.4] # probability
		self.delta: dict = { 1: 0, 2: 0 } # Δ₁=|M(X)-m|, Δ₂=|D(X)-g|

	@staticmethod
	def k_list(x: list, i: list) -> list:
		k: list = []
		for j in range(len(x)):
			k.append(0)
		for j in range(len(i)):
			k[i[j]] += 1
		return k

	@staticmethod
	def table_eval(self, math) -> float:
		result: float = 0
		k: list = RandomCalculus.k_list(math.x, self.i)
		for i in range(len(math.x)):
			result += math.x[i] * k[i]
		result /= self.numbers
		return result

	@staticmethod
	def table_diseval(self, math) -> float:
		result: float = 0
		k: list = RandomCalculus.k_list(math.x, self.i)
		for i in range(len(math.x)):
			result += (math.x[i] ** 2) * k[i]
		result /= self.numbers
		return result

	def set_expecting(self, method) -> None: self.expecting = method
	def set_dispersing(self, method) -> None: self.dispersing = method
	def set_evaluating(self, method) -> None: self.evaluating = method
	def set_dis_evaluating(self, method) -> None: self.dis_evaluating = method

	def to_list(self, name: str) -> list:
		f: list = Text.format_columns(Resources.Fields[name]["initial"])
		return [f[0] % (self.m_expect), f[1] % (self.m_eval),
			f[2] % (self.delta[1]), f[3] % (self.dispersia),
			f[4] % (self.ground), f[5] % (self.delta[2])]

	def expectation(self, k: int) -> None: # Σ(xₖpₖ)
		self.m_expect += self.x[k] * self.p[k]

	def set_first_delta(self) -> None: # Δ₁=|M(X)-m|
		self.delta[1] = abs(self.m_expect - self.m_eval)

	def get_dispersia(self, k: int) -> None: # Σ(pₖ(xₖ - M)²)
		self.dispersia += self.p[k] * self.x[k] ** 2

	def get_dispersia_end(self) -> None: # Σ(pₖ(xₖ - M)²)
		self.dispersia -= self.m_expect ** 2

	def set_second_delta(self) -> None: # Δ₂=|D(X)-g|
		self.delta[2] = abs(self.dispersia - self.ground)

	def evaluation(self, k: int) -> None: # Σ(xₖ)
		# print("X: ", self.x[k])
		self.m_eval += self.x[k]

	def evaluation_end(self, n: int) -> None: # m / N
		self.m_eval /= 1 if n == 0 else n

	def dispersia_ground(self, k: int) -> None: # Σ(xₖ²)
		self.ground += self.x[k] ** 2

	def dispersia_ground_end(self, n: int) -> None: # g / (N - 1) - (N / (N - 1))m²
		# self.ground = self.ground / n - self.m_eval ** 2
		n1: int = n - 1 if n - 1 == 0 else 1
		self.ground = (self.ground / n1) - (n / n1) * (self.m_eval ** 2)
