class PositiveValue:
    @classmethod
    def verify_coord(cls, param):
        if not isinstance(param, (int, float)) or param <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Triangle:
    a = PositiveValue()
    b = PositiveValue()
    c = PositiveValue()

    def __init__(self, a, b, c):
        self._points = (a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        # избегаем рекурсивного вызова метода __setattr__ при установке скрытых атрибутов
        if key in ('_points', '_a', '_b', '_c'):
            super().__setattr__(key, value)
            return

        index = {'a': 0, 'b': 1, 'c': 2}[key]
        current_values = list(self._points)
        current_values[index] = value

        if any(value >= sum(current_values) - value for value in current_values):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

        self._points = tuple(current_values)
        super().__setattr__(key, value)

    def __call__(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def __len__(self):
        return int(self.a + self.b + self.c)
