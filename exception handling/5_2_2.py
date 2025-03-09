def to_number(value):
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        raise


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'Point: x = {self._x}, y = {self._y}'


try:
    x, y = input().split()
    pt = Point(to_number(x), to_number(y))
except ValueError:
    pt = Point()

finally:
    print(pt)
