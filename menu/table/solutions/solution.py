from random import random
from menu.table.solutions.calculus import RandomCalculus

class RandomDistribution:
    def __init__(self, args: dict) -> None:
        self.math = RandomCalculus(args["X"], args["p"])
        self.i: list = []
        self.matrix: list = []
        self.numbers: int = args["N"] # 100 # N
        self.quantity: int = args["q"] # 14 # q

    def reverse_method(self, value: float) -> float:
        i: int = len(self.math.p)
        segment: float = sum(self.math.p)
        found: bool = value == segment
        self.math.is_one_probability(segment)
        while i > 0 and not found:
            i -= 1
            current: float = segment - self.math.p[i]
            found = value >= current and value < segment
            segment = current
        return i

    def generate_random(self) -> None:
        for i in range(self.numbers):
            self.i.append(self.reverse_method(random()))
        self._calculate()

    def output_first_quantity(self) -> None:
        columns: int = 10
        table_length: int = int(self.quantity / columns)
        for r in range(table_length):
            row: list = []
            for c in range(columns):
                i: int = self.i[r * columns + c]
                row.append(self.math.x[i])
            for i in range(len(row), columns):
                row.append(0)
            self.matrix.append(row)

    def sigma(self, formula) -> None: # Σ
        for j in range(self.numbers): formula(self.i[j])

    def _calculate(self) -> None:
        self.math.check_count(self.numbers, 1)
        self.sigma(lambda i: self.math.expectation(i))
        self.sigma(lambda i: self.math.get_dispersia(i))
        self.sigma(lambda i: self.math.evaluation(i))
        self.math.evaluation_end(self.numbers)
        self.sigma(lambda i: self.math.dispersia_ground(i))
        self.math.dispersia_ground_end(self.numbers)
