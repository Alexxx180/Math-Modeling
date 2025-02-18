from random import random
from common.commander.resources import Resources

class RandomSelection:
	def __init__(self, n: int, q: int) -> None:
		self.r: list = []
		self.numbers: int = n  # 100 # N
		self.quantity: int = q # 14 # q

	def generate_values(self, method) -> None:
		existing: dict = {}
		x: list = []
		j: int = 0
		self.i: list = []
		for i in range(self.numbers):
			r: float = method(random())
			if not r in existing:
				existing[r] = j
				x.append(r)
				self.i.append(j)
				j += 1
			else:
				self.i.append(existing[r])
		return x

	def generate_random(self, method) -> None:
		self.i = [method(random()) for i in range(self.numbers)]

	def sigma(self, formula) -> None: # Σ
		for j in range(self.numbers): formula(self.i[j])

	def preview(self, math) -> None:
		q: int = self.quantity
		table: dict = Resources.Fields["table"]
		columns: int = max(len(table["Source"]) - 1, 1)
		table_length: int = int(q / columns)

		if q % columns != 0: table_length += 1

		x = math.x
		if hasattr(math, 'xf'):
			x = math.xf

		for r in range(table_length):
			row: list = []

			for c in range(min(q, columns)):
				i: int = self.i[r * columns + c]
				row.append(x[i])

			for i in range(len(row), columns):
				row.append(table["No-value"])

			self.r.append(row)
			q -= columns

	def calculate(self, math) -> None:
		if math.expecting == None:
			self.sigma(lambda i: math.expectation(i))
		else:
			math.expect = math.expecting()

		if math.dispersing == None:
			self.sigma(lambda i: math.get_dispersia(i))
		else:
			math.dispersia = math.dispersing(math.expect)

		self.sigma(lambda i: math.evaluation(i))
		math.evaluation_end(self.numbers)
		self.sigma(lambda i: math.dispersia_ground(i))
		math.dispersia_ground_end(self.numbers)
		self.preview(math)
