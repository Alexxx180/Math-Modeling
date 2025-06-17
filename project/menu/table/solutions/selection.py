from menu.table.solutions.structure.preview import get_preview
from menu.table.solutions.structure.generate import get_random, generate_random_values, sigma

class RandomSelection:
	def __init__(self, n: int, q: int) -> None:
		self.r: list = []
		self.numbers: int = n  # 100 # N
		self.quantity: int = q # 14 # q

	def preview(self, math) -> None: get_preview(self, math)
	def generate_values(self, method) -> list:
		return generate_random_values(self, method)

	def generate_random(self, method) -> None:
		self.i = [get_random(method) for i in range(self.numbers)]

	def set_math_expectation(self, math) -> None:
		if math.expecting == None:
			# sigma(self.numbers, self.i, lambda i: math.expectation(i))
			for i in range(0, len(math.x)): math.expectation(i)
		else:
			math.m_expect = math.expecting()

	def set_dispersia(self, math) -> None:
		if math.dispersing == None:
			# sigma(self.numbers, self.i, lambda i: math.get_dispersia(i))
			for i in range(0, len(math.x)): math.get_dispersia(i)
			math.get_dispersia_end()
		else:
			math.dispersia = math.dispersing(math.m_expect)

	def set_math_evaluation(self, math) -> None:
		if math.evaluating == None:
			sigma(self.numbers, self.i, lambda i: math.evaluation(i))
		else:
			math.m_eval = math.evaluating(self, math)
		math.evaluation_end(self.numbers)
		math.set_first_delta()

	def set_dispersia_evaluation(self, math) -> None:
		if math.dis_evaluating == None:
			sigma(self.numbers, self.i, lambda i: math.dispersia_ground(i))
			math.dispersia_ground_end(self.numbers)
		else:
			math.ground = math.dis_evaluating(self, math)
		math.set_second_delta()

	def calculate(self, math) -> None:
		self.set_math_expectation(math)
		self.set_dispersia(math)
		self.set_math_evaluation(math)
		self.set_dispersia_evaluation(math)
		self.preview(math)
