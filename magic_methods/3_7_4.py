class Ellipse:
    def __init__(self, *args):
        if not args:
            pass
        else:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return all(hasattr(self, elem) for elem in ('x1', 'y1', 'x2', 'y2'))

    def get_coords(self):
        try:
            return self.x1, self.y1, self.x2, self.y2
        except:
            raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for elem in lst_geom:
    if elem:
        elem.get_coords()
