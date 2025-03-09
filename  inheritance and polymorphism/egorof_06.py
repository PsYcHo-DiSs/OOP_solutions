class Circle:
    PI = 3.14

    def __new__(cls, radius, *args, **kwargs):
        cls._radius = radius
        cls._diameter = 2 * radius
        cls.get_radius = lambda self: self._radius
        cls.get_diameter = lambda self: self._diameter
        cls.get_area = lambda self: self.PI * self._radius ** 2
        cls.get_perimeter = lambda self: 2 * self.PI * self._radius
        instance = super().__new__(cls)
        return instance
