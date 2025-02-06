from numpy import arange

class Points:
    def __init__(self, ends, function: callable):
        self.task = function
        self.step = 0.0001
        if isinstance(ends, list) or isinstance(ends, tuple):
            self.__range(ends[0], ends[1])
        else:
            self.__range(-ends, ends)
        self.__function()

    def __range(self, a: float, b: float):
        self.a = a
        self.b = b

    def __function(self):
        self.X = [x for x in arange(self.a, self.b, self.step)]
        self.Y = [self.task(x) for x in self.X]
