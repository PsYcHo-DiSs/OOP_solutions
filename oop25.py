class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if self.__class__.__is_correct(x) and self.__class__.__is_correct(y):
            self.__x = x
            self.__y = y
        else:
            self.__x = self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__class__.__is_correct(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__class__.__is_correct(value):
            self.__y = value

    @classmethod
    def __is_correct(cls, digit):
        return isinstance(digit, (int, float)) and cls.MIN_COORD <= digit <= cls.MAX_COORD

    @staticmethod
    def norm2(vector):
        return (vector.x * vector.x) + (vector.y * vector.y)
