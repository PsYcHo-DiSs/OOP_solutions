class Descriptor:

    def __init__(self, type, message):
        self.type = type
        self.message = message

    def __is_valid(self, value):
        if not isinstance(value, self.type):
            raise ValueError(f'возможны только {self.message} значения')

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__is_valid(value)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        delattr(instance, self.name)


class CellInteger:
    value = Descriptor(int, 'целочисленные')

    def __init__(self, start_value=0):
        self.value = start_value


class CellString:
    value = Descriptor(str, 'строчные')

    def __init__(self, start_value='0'):
        self.value = start_value


class TableValues:

    def __new__(cls, *args, **kwargs):
        if not kwargs:
            raise ValueError('параметр cell не указан')
        return super().__new__(cls)

    def __init__(self, rows, cols, cell=CellInteger):
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(self.cols)) for _ in range(self.rows))

    def __getitem__(self, item):
        r, c = item
        return self.cells[r][c].value

    def __setitem__(self, key, value):
        r, c = key
        self.cells[r][c].value = value
