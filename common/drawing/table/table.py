from common.handlers.interaction import pause
from common.drawing.table.struct import TableStruct
from common.drawing.table.defaults import TableDefaults

class Table:
    def __init__(self, fields: list = [], title: str = ""):
        if title == "" and len(fields) != 0:
            title = fields.pop(0)
        self.alignment = { 'Left': 'l', 'Center': 'c', 'Right': 'r' }
        self.fields = fields
        self.table = TableDefaults(title, self.alignment)
        self.struct = TableStruct()

    def floats(self, symbols: str):
        self.table.float_format = symbols
        return self

    def align(self, side: str, field: str = ''):
        if field == '':
            self.table.align = self.alignment[side]
        else:
            self.table.align[field] = self.alignment[side]
        return self

    def row(self, values: list):
        self.table.field_names = self.fields
        self.table.add_row(values)
        #self.struct.row(self.table, x)
        return self

    def rows(self, values:list):
        self.table.field_names = self.fields
        self.struct.rows(self.table, values)
        return self

    def columns(self, start: int, memory):
        self.struct.columns(self.fields, self.table, start, memory)
        return self

    def matrix(self, rows: list, head: str = 'x'):
        self.struct.matrix(self.table, rows, head)
        return self

    def show(self):
        print(self.table)
        return self

    def clear(self):
        self.table.clear_rows()
        return self

    def print(self, text: str = ""):
        print(text)
        return self

    def pause(self, text: str = ""):
        pause(text)
        return self
