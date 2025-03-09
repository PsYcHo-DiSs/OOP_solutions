class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Box3D(self.width * other, self.height * other, self.depth * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        if isinstance(other, int):
            return Box3D(self.width // other, self.height // other, self.depth // other)
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, int):
            return Box3D(self.width % other, self.height % other, self.depth % other)
        return NotImplemented