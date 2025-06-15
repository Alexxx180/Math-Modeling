def get_probability_sum(probability: list) -> float:
	segment: float = sum(probability)
	# if segment != 1: print("Probability sum is: ", segment)
	return segment

def method_reverse(self, value: float) -> float:
	i: int = len(self.math.p)
	segment: float = get_probability_sum(self.math.p)
	found: bool = value == segment

	while i > 0 and not found:
		i -= 1
		# print("p: ", self.math.p[i], " s: ", segment)
		current: float = segment - self.math.p[i]
		found = current <= value and value < segment
		segment = current

	return i
