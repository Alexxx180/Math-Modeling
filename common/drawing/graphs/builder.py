from common.commander.resources import Resources
from common.drawing.graphs.canvas import Canvas
from common.drawing.primitives.points import Points
from common.drawing.primitives.point import Point

class CanvasBuilder:
    def __init__(self):
        self.canvas = Canvas()
        self.task = None

    def space(self, space):
        self.canvas.space = space
        return self

    def graph(self, plot):
        self.canvas.space.set_graph(plot)
        return self

    def select(self, i: int):
        self.canvas.space.select(i)
        return self

    def formula(self, task: callable):
        self.task = task
        return self

    def mark(self, args, size: int = 0):
        if self.task == None:
            self.basis = Point(args, size)
        else:
            self.basis = Points(args, self.task)
        return self

    def __text(self, name: str):
        return Resources.Texts[self.canvas.space.name][name]

    def label(self, name: str, i: int = -1):
        setting = (self.basis, self.__text(name), i)
        self.canvas.settings.append(setting)
        return self

    def plane(self, i: int = -1):
        self.canvas.planes.append((self.basis, i))
        return self

    def entitle(self, name: str):
        self.canvas.space.plot.window(self.__text(name))
