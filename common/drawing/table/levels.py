class TableLevels:
    def __init__(self):
        self.single = lambda t, i, r: t.add_row([i, r])
        self.double = lambda t, i, r: t.add_row([i, r[0], r[1]])

    def __append(self, table, rows: list, add: callable):
        for index, row in enumerate(rows):
            add(table, index + 1, row)

    def __appendix(self, table, row: list, no: int):
        row.insert(0, no)
        table.add_row(row)

    def count(self, levels):
        if isinstance(levels, list):
            return 1 + max(self.count(level) for level in levels)
        return 0

    def dimension(self, table, rows: list):
        if len(rows) == 1:
            self.__append(table, rows, self.single)
        else:
            table.add_row(rows)

    def dimensions(self, table, row: list):
        f = self.double if len(row[0]) != 2 else self.__appendix
        self.__append(table, row, f)
        return self
