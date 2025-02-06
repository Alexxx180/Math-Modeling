from sympy import Symbol, integrate
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

def invokation(derive, *symbols) -> callable:
    if derive == '0':
        return lambda x: 0
    #print(derive)
    return lambdify(symbols, derive)
