from common.commander.resources import Resources

class Printer:
    def __init__(self, name: str):
        self.name = name
        self.order: list = [print, None, None]

    def __get(self, keys: list):
        field = Resources.Texts[self.name]
        for key in keys:
            field = field[key]
        return field

    def edit(self, position: int, key: str):
        self.order[1][position] = key
        return self

    def act(self, function: callable):
        self.order[0] = function
        return self

    def keys(self, *keys):
        self.order[1] = list(keys)
        return self

    def args(self, *values):
        self.order[2] = values
        return self

    def text(self):
        return self.__get(self.order[1])

    def print(self):
        text: callable = self.order[0]
        field = self.__get(self.order[1])
        args: tuple = self.order[2]
        if len(args) == 0:
            text(field)
        else:
            text(field.format(*args))
        return self
