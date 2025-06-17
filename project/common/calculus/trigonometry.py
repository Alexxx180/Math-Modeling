from sympy import Symbol, integrate
from sympy.abc import x
from sympy.utilities import lambdify
from sympy.parsing.sympy_parser import parse_expr

def express(formula: str):
	return parse_expr(formula)

def form(derivative, *symbols) -> str:
	return derivative.diff(*symbols)

def formulate(text, count: int, *symbols) -> str:
	derivative = express(text)

	try:
		for i in range(count):
			derivative = form(derivative, *symbols)
	except ValueError:
		return '0'

	return derivative

def invokation(expression, *symbols) -> callable:
	match expression:
		case '0':
			return lambda x: 0
		case _:
			return lambdify(symbols, expression)

def integral(formula: str, ab: tuple) -> callable:
	return integrate(formula, (x, ab[0], ab[1]))

def un_integral(formula: str):
	return integrate(formula, x)
