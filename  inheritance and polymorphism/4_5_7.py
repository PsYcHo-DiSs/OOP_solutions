class Track:
    def __init__(self, *args):
        if len(args) == 2:
            x, y = args[0], args[1]
            self.__points = [PointTrack(x, y)]
        if len(args) > 2:
            self.__points = list()
            self.__points.extend(args)

    def add_back(self, pt):
        self.__is_point_track(pt)
        self.__points.append(pt)

    def add_front(self, pt):
        self.__is_point_track(pt)
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)

    @staticmethod
    def __is_point_track(point):
        if not isinstance(point, PointTrack):
            raise TypeError('операции с точкой возможны только если объект является классом PointTrack')

    @property
    def points(self):
        return tuple(self.__points)


class PointTrack:
    def __init__(self, x, y):
        self.__is_valid_coord(x)
        self.__is_valid_coord(y)
        self.x = x
        self.y = y

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'

    @staticmethod
    def __is_valid_coord(value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')
