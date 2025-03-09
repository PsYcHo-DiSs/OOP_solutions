class ColourComponent:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __get__(self, instance, owner):
        return int(instance.hex[self.start:self.end], 16)


class Colour:
    r = ColourComponent(1, 3)
    g = ColourComponent(3, 5)
    b = ColourComponent(5, 7)

    def __init__(self, hex):
        self.hex = hex
