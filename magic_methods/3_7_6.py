class Vector:
    def __init__(self, *args):
        if not all(type(elem) in (int, float) for elem in args):
            raise TypeError('несоответствующий тип данных при инициализации')
        self.coords = list(args)

    def __is_eq_dimension(self, other):
        self.__is_vector(other)
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    @staticmethod
    def __is_vector(other):
        if not isinstance(other, Vector):
            raise TypeError('несоответствующий тип данных')

    def __add__(self, other):
        self.__is_eq_dimension(other)
        return Vector(*tuple(x1 + y1 for x1, y1 in zip(self.coords, other.coords)))

    def __sub__(self, other):
        self.__is_eq_dimension(other)
        return Vector(*tuple(x1 - y1 for x1, y1 in zip(self.coords, other.coords)))

    def __mul__(self, other):
        self.__is_eq_dimension(other)
        return Vector(*tuple(x1 * y1 for x1, y1 in zip(self.coords, other.coords)))

    def __iadd__(self, other):
        if type(other) in (int, float):
            self.coords = [elem + other for elem in self.coords]
            return self
        self.__is_eq_dimension(other)
        self.coords = [x1 + y1 for x1, y1 in zip(self.coords, other.coords)]
        return self

    def __isub__(self, other):
        if type(other) in (int, float):
            self.coords = [elem - other for elem in self.coords]
            return self
        self.__is_eq_dimension(other)
        self.coords = [x1 - y1 for x1, y1 in zip(self.coords, other.coords)]
        return self

    def __eq__(self, other):
        try:
            self.__is_eq_dimension(other)
        except ArithmeticError:
            return False

        return all(el1 == el2 for el1, el2 in zip(self.coords, other.coords))
