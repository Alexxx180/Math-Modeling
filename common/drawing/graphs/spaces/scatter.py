from common.commander.resources import Resources

class ScatterSpace:
    def __init__(self, name: str, color: str = 'red'):
        self.name = name
        self.color = color

    def set_graph(self, graph):
        self.plot = graph

    def select(self, i: int):
        self.plot.select(i)

    def draw(self, basis: list, line: float, label: str):
        self.plot.ax.plot(basis, line, label=label, linestyle='--')

    def scatters(self, x, y, color = ''):
        if color == '': color = self.color

        self.plot.ax.scatter(x, y, color=color,
            label=Resources.Texts[self.name]['Point'])

    def show(self):
        self.plot.ax.legend()

    def render(self, order: tuple):
        self.draw(order[0], order[1], order[2])
        self.scatters(order[3], order[4], order[5])
