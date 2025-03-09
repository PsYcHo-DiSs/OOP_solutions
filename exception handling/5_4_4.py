class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    def _valid_diapason(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellException('значение выходит за допустимый диапазон')

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._valid_diapason(value)
        setattr(self, '_value', value)


class CellInteger(Cell):
    def _valid_diapason(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')


class CellFloat(Cell):
    def _valid_diapason(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')


class CellString(Cell):
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    def _valid_diapason(self, value):
        if not self._min_length <= len(value) <= self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')


class TupleData:
    def __init__(self, *args):
        if not all(isinstance(el, (CellInteger, CellFloat, CellString)) for el in args):
            raise ValueError('Все элементы должны быть экземплярами классов CellInteger, CellFloat или CellString')
        self._cells = list(args)

    def __getitem__(self, index):
        self._validate_index(index)
        return self._cells[index].value

    def __setitem__(self, index, value):
        self._validate_index(index)
        self._cells[index].value = value

    def __len__(self):
        return len(self._cells)

    def __iter__(self):
        for cell in self._cells:
            yield cell.value

    def _validate_index(self, indx_value):
        if type(indx_value) != int:
            raise TypeError('Индекс должен быть целым числом')
        if not (0 <= indx_value < len(self._cells)):
            raise IndexError('Индекс выходит за допустимый диапазон')
