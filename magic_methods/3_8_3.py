class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self._arr = [self.cell(0) for _ in range(max_length)]

    def __str__(self):
        return " ".join(str(cell.start_value) for cell in self._arr)

    def __getitem__(self, item):
        if type(item) == int and 0 <= item < self.max_length:
            return self._arr[item].start_value
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __setitem__(self, key, value):
        if type(key) != int or not (0 <= key < self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

        self._arr[key].start_value = value


class Integer:
    def __init__(self, start_value=0):
        self._start_value = start_value

    @property
    def start_value(self):
        return self._start_value

    @start_value.setter
    def start_value(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        self._start_value = value