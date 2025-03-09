class Rect:
    def __init__(self, x, y, width, height):
        if not all(isinstance(i, (int, float)) for i in (x, y, width, height)) or width <= 0 or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')

        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        """Проверяет пересечение текущего прямоугольника с другим rect"""
        if not (self._x + self._width <= rect._x or
                rect._x + rect._width <= self._x or
                self._y + self._height <= rect._y or
                rect._y + rect._height <= self._y):
            raise TypeError('прямоугольники пересекаются')


# Создание списка прямоугольников
lst_rect = [Rect(0, 0, 5, 3),
            Rect(6, 0, 3, 5),
            Rect(3, 2, 4, 4),
            Rect(0, 8, 8, 1)]

# Отбираем непересекающиеся прямоугольники
lst_not_collision = []
for i, rect in enumerate(lst_rect):
    try:
        for j, other in enumerate(lst_rect):
            if i != j:
                rect.is_collision(other)
        lst_not_collision.append(rect)
    except TypeError:
        pass