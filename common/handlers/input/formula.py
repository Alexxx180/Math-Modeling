p: str = 'p'

def extract(args: list, constant: str):
    i: int = constant.index(p)
    if i == 0:
        args.append(1)
    else:
        args.append(int(constant[:i]))

def from_formula(formula: str) -> list:
    if p not in formula:
        return [float(x) for x in formula.split()]

    args: list = []; c: list = []

    for expression in formula.split('+'):
        negative = expression.split('-')
        c.append(negative[0].strip())
        for i in range(1, len(negative)):
            c.append('-' + negative[i].strip())

    for constant in c:
        if p not in constant:
            args.append(int(constant))
        else:
            extract(args, constant)

    # (1, 8, 32, 80, 100) # ...split
    #"A": "p3 + 2p2 + 2p + 1",
    #"B": "p4 + p3 + 3p2 + 2p + 1"

    return args
