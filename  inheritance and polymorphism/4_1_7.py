class Vector:
    def __init__(self, *args):
        self._coords = list(args)

    def __validate_dimensions(self, other):
        if len(self._coords) != len(other._coords):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return tuple(self._coords)

    @staticmethod
    def has_float_coord(coords):
        return any(isinstance(coord, float) for coord in coords)

    def __add__(self, other):
        self.__validate_dimensions(other)
        result_coords = [a + b for a, b in zip(self._coords, other._coords)]
        return VectorInt(*result_coords) if not self.has_float_coord(result_coords) else Vector(*result_coords)

    def __sub__(self, other):
        self.__validate_dimensions(other)
        result_coords = [a - b for a, b in zip(self._coords, other._coords)]
        return VectorInt(*result_coords) if not self.has_float_coord(result_coords) else Vector(*result_coords)


class VectorInt(Vector):
    def __init__(self, *args):
        if any(not isinstance(coord, int) for coord in args):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)