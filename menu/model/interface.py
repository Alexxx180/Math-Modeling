from sympy.abc import x, r
from sympy import solve
from common.commander.switch import View
from common.flow.texts.table import Text
from menu.table.solutions.solution import RandomDistribution
from common.calculus.trigonometry import form, invokation, express, integral
from common.commander.resources import Resources

POSITIVE: int = 1

"""
This program takes a probability value table, generate random numbers.
Then calculate math expectation, dispersia, and evaluate both results
"""
def RandomModelReverseMethod(name: str, args: list) -> None:
	ab: tuple = (1, 2)
	formula: str = Resources.Formula["continuous"]
	print("Formula: ", formula)
	inverse = solve(express(formula) - r, x)[POSITIVE]
	print("Inverse: ", str(inverse))
	result = integral(express("x * (" + formula + ")"), ab)
	print("Integral: ", result)

	f: str = "(x ** 2) * (" + formula + ")"
	invf = invokation(express(str(inverse)))
	print("Inverse result: ", invf(1))

	table = RandomDistribution(args)
	table.method = lambda v: invf(v)
	table.expecting = lambda: result
	table.dispersing = lambda: integral(express(f), ab) - table.math.expect ** 2
	table.start()
	text = Text(name)
	text.table(table)
	text.research(table.math)

	if View('Table', name):
		text.source(table.init.r)

	text.pause()

def get_result(args: list) -> str:
	table = RandomDistribution(args).start()
	math = table.math
	init = table.init
	result: list = [math.expect, math.dispersia, math.eval, math.ground]
	result.extend([init.numbers, init.quantity, str(math.x), str(math.p), str(init.r)])
	return " - ".join(result)
