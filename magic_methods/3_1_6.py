class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__getattribute__("__x")

    @x.setter
    def x(self, x):
        self.__setattr__("__x", x)

    @property
    def y(self):
        return self.__getattribute__("__y")

    @y.setter
    def y(self, y):
        self.__setattr__("__y", y)

    @property
    def radius(self):
        return self.__getattribute__("__radius")

    @radius.setter
    def radius(self, radius):
        self.__setattr__("__radius", radius)

    def __setattr__(self, key, value):
        if type(value) not in (float, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value < 0:
            return self.__radius

        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False
