from common.drawing.table.levels import TableLevels

class TableStruct:
    def __init__(self):
        self.levels = TableLevels()

    def row(self, table, values: list):
        levels = self.levels.count(values)
        if levels == 1:
            self.levels.dimension(table, values)
        elif levels > 1:
            self.levels.dimensions(table, values)
        return self

    def rows(self, table, rows: list):
        for row in rows:
            table.add_row(row)

    def column(self, field: str, table, values: list):
        table.add_column(field, values)
        return self

    def columns(self, fields: list, table, start: int, memory: list):
        end: int = len(memory)
        for i in range(start, end):
            self.column(fields[i], table, memory[i])
        return self

    def matrix(self, table, rows: list, head: str = 'x'):
        count: int = len(rows[0]) - 1
        fields: list = [f"{head}{i + 1}" for i in range(count)]
        fields.append(head.upper())
        table.field_names = fields
        for row in rows:
            table.add_row(row)
