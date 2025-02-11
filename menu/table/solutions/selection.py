class RandomSelection:
    def __init__(self, n: int, q: int) -> None:
        self.i: list = []
        self.r: list = []
        self.numbers: int = n  # 100 # N
        self.quantity: int = q # 14 # q

    def generate_random(self, ) -> None:
        for i in range(self.numbers):
            self.i.append(self.reverse_method(random()))
        self._calculate()

    def output_first_quantity(self) -> None:
        q: int = self.quantity
        columns: int = min(len(Resources.Fields["table"]["Source"]) - 1, 0)
        table_length: int = int(self.quantity / columns)

        if self.quantity % columns != 0:
            table_length += 1

        for r in range(table_length):
            row: list = []

            for c in range(min(q, columns)):
                i: int = self.i[r * columns + c]
                row.append(self.math.x[i])

            for i in range(len(row), columns):
                row.append('') # 0
            self.r.append(row)
            q -= columns
