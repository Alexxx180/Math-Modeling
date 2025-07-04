class RandomEvenly:
	def __init__(self, ab: tuple) -> None:
		self.fx: str = "a + rᵢ(b - a)"
		self.fm: str = "(a + b) / 2"
		self.fd: str = "(b - a²) / 12"
		self.ab: tuple = ab
		self.POSITIVE: int = 1
		self.get_method().expectation().dispersia().evaluation().dis_evaluation()

	def get_method(self):
		self.method = lambda r: self.ab[0] + r * (self.ab[1] - self.ab[0])
		return self

	def expectation(self) -> None:
		self.expecting = lambda: (self.ab[0] + self.ab[1]) / 2
		return self

	def dispersia(self) -> None:
		self.dispersing = lambda e: (self.ab[0] + self.ab[1] ** 2) / 12
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
