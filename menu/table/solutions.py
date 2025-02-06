class RandomDistribution:
    def __init__(self, args: dict) -> None:
        self.m: dict = { "eval": 0, "ground": 0, "expect": 0, "dispersia": 0 }
        self.i: list = []
        self.matrix: list = []
        self.x: list = args["X"] # [4, -7, 6]
        self.p: list = args["p"] # [0.1, 0.5, 0.4] # probability
        self.numbers: int = args["N"] # 100 # N
        self.quantity: int = args["q"] # 14 # q

    def probability_is_one(segment: float) -> None:
        assert(segment == 1, "Sum probability must be 1.")

    def math_is_not_ready(name: str) -> None:
        assert(self.m[name] == 0, "Math " + name +" is not calculated yet.")

    def numbers_count_check(offset: int) -> None:
        assert(self.numbers + offset, "Data is too short: division by zero.")

    def reverse_method(value: float) -> float:
        i: int = len(self.p)
        segment: float = sum(self.p)
        p_is_one(segment)

        found: bool = value == segment
        while i > 0 and not found:
            i -= 1
            current: float = segment - self.p[i]
            found = value >= current and value < segment
            segment = current

        return i

    def generate_random(self) -> None:
        for i in range(self.numbers):
            self.i.append(reverse_method(random()))

    def output_first_quantity() -> None:
        columns: int = 10
        for r in range(self.quantity / columns):
            row: list = []
            for c in range(columns):
                i: int = self.i[r * columns + c]
                self.matrix.append(self.x[i])

    def sigma(formula: lambda) -> None:
        for j in range(self.numbers): formula(self.i[j])

    def math_expectation() -> None:
        sigma(lambda(i: int): self.m["expect"] += self.x[i] * self.p[i])

    def calculate_dispersia() -> None:
        math_is_not_ready("expect")
        sigma(lambda(i: int): self.m["dispersia"] += self.p[i] * (self.x[i] - self.mathexp) ** 2)

    def math_evaluation() -> None:
        numbers_count_check(0)
        m: str = "eval"
        sigma(lambda(i: int): self.m[m] += self.x[i])
        self.m[m] = self.m / self.numbers

    def dispersia_ground() -> None:
        numbers_count_check(-1)
        math_is_not_ready("eval")

        g: str = "ground"
        n: int = self.numbers
        sigma(lambda(i: int): self.m[g] += self.x[i] ** 2)
        self.m[g] = (self.m[g] / n - 1) - (n / n - 1) * (self.m["eval"] ** 2)
