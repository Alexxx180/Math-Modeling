from random import random

def append_unique(x: dict, value: float, i: list) -> None:
	x["existing"][value] = x["counter"]
	x["values"].append(value)
	i.append(x["counter"])
	x["counter"] += 1

def get_random(method): return method(random())

def generate_random_values(self, method) -> list:
	x: dict = { "existing": {}, "values": [], "counter": 0 }
	self.i: list = []
	for i in range(self.numbers):
		value: float = get_random(method)
		#print("r: ", r, "ex: ", existing)
		if not value in x["existing"]:
			append_unique(x, value, self.i)
		else:
			self.i.append(x["existing"][value])
	return x["values"]

def sigma(N: int, i: list, formula) -> None: # Σ(x)
#	print("LEN: ", len(i), " N: ", N)
	for j in range(N):
		# print("i: ", i[j], " - j: ", j)
		formula(i[j])
