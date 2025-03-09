from random import randint, choice


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


classes = [Line, Rect, Ellipse]
elements = [choice(classes)(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)) for i in range(217)]

for elem in elements:
    if isinstance(elem, Line):
        setattr(elem, 'sp', (0, 0))
        setattr(elem, 'ep', (0, 0))
