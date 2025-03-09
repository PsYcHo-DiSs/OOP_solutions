import numpy as np


class RangeValidator:
    def __init__(self, start, stop):
        self.start = start
        self.end = stop

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, f'_{self.name}')

    def __set__(self, instance, value):
        self._is_valid_type(value)
        self._is_valid_range(value)
        setattr(instance, f'_{self.name}', value)

    def _is_valid_type(self, value):
        if type(value) != int:
            raise TypeError('Неправильный тип данных')

    def _is_valid_range(self, value):
        if value not in np.arange(self.start, self.end):
            raise ValueError(f"Значение должно быть между {self.start} и {self.end}")
