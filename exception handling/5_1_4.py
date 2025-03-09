# здесь объявляйте класс Triangle
class Triangle:
    def __init__(self, a, b, c):
        if any(type(n) not in (int, float) or n <= 0 for n in (a, b, c)):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

        self._a = a
        self._b = b
        self._c = c


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5),
              (7, 4, 6)]  # эту строчку не менять (переменную input_data также не менять)

# здесь формируйте список lst_tr
lst_tr = list()
for elem in input_data:
    try:
        lst_tr.append(Triangle(*elem))
    except (TypeError, ValueError):
        continue
