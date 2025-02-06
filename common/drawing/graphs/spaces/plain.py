from common.drawing.drawing import *

class PlainSpace:
    def __init__(self, name: str, color = 'red'):
        self.name = name
        self.color = color
        self.fontsize = 10
        self.style = 'dashed'
        self.align = { 'horizontal': 'left', 'vertical': 'bottom' }

    def set_graph(self, graph):
        self.plot = graph

    def select(self, i: int):
        self.plot.select(i)

    def line(self, x: float, y: float):
        self.points = (y, 0)
        self.plot.vlines(self.points, x, self.style, self.color)

        for point in self.points:
            self.plot.make(x, point, Points[self.color])

        if abs(self.points[0]) > 0.01:
            self.plot.text(self.points, x, self.align, self.fontsize)

    def lines(self, values: tuple, f: callable):
        for x in values: self.line(x, f(x))

    def show(self): pass

    def render(self, order):
        if isinstance(order, int):
            self.plot.select(order)
            return

        basis = order[0]
        drawing = order[1]

        if len(order) == 3:
            self.color = order[2]
        if isinstance(basis, tuple):
            self.lines(basis, drawing)
        else:
            self.line(basis, drawing)
