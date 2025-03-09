class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.__rows = rows
        self.__cols = cols
        self.__type_data = type_data
        self.__table = tuple(tuple(Cell() for _ in range(self.__cols)) for _ in range(self.__rows))

    def __is_valid_indx(self, index):
        r, c = index
        if not (type(r) == int and type(c) == int) or not (0 <= r < self.__rows) or not (0 <= c < self.__cols):
            raise IndexError('неверный индекс')

    def __is_valid_value(self, value):
        if not isinstance(value, self.__type_data):
            raise TypeError('неверный тип присваиваемых данных')

    def __getitem__(self, item):
        self.__is_valid_indx(item)
        r, c = item
        return self.__table[r][c].data

    def __setitem__(self, key, value):
        self.__is_valid_indx(key)
        self.__is_valid_value(value)
        r, c = key
        self.__table[r][c].data = value

    def __iter__(self):
        for row in self.__table:
            yield (elem.data for elem in row)


class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
