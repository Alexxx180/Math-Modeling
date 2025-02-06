class Ends:
    def __init__(self, start, end = None):
        if isinstance(start, tuple) or isinstance(start, list):
            self.start = start[0]
            self.end = start[1]
        elif end is None:
            self.start = -start
            self.end = start
        else:
            self.start = start
            self.end = end

    def based(self, f: callable):
        return Ends(f(self.start), f(self.end))

    def size(self) -> float:
        return self.end - self.start

    def sub(self) -> float:
        return self.start - self.end

    def sum(self) -> float:
        return self.start + self.end

    def margin(self, margin: float = 0.0) -> tuple:
        return (self.start - margin, self.end + margin)
