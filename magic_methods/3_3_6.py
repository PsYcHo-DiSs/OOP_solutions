from math import sqrt
from functools import reduce


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            dimension = args[0]
            self.dct_shape = {k: 0 for k in range(1, dimension + 1)}
        else:
            self.dct_shape = {k: v for k, v in enumerate(args, start=1)}

    def set_coords(self, *args):
        if len(args) > len(self.dct_shape.keys()):
            args = args[:len(self.dct_shape.keys())]
        for k, v in enumerate(args, start=1):
            self.dct_shape[k] = v

    def get_coords(self):
        return tuple(self.dct_shape.values())

    def __len__(self):
        return len(self.dct_shape)

    def __abs__(self):
        items = self.get_coords()
        return sqrt(reduce(lambda total, item: total + (item * item), items))
