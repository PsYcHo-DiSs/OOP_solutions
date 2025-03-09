class IntegerValue:
    @classmethod
    def __is_valid(cls, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__is_valid(value)
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell):
        self.rows = rows
        self.cols = cols
        if not cell:
            raise ValueError('параметр cell не указан')
        self.cells = tuple(tuple(cell() for _ in range(self.cols)) for _ in range(self.rows))

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value
