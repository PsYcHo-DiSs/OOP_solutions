class Digit:
    def __init__(self, value):
        self._is_valid_value(value)
        self.value = value

    @staticmethod
    def _is_valid_value(value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    @staticmethod
    def _is_valid_value(value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    @staticmethod
    def _is_valid_value(value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    @staticmethod
    def _is_valid_value(value):
        super()._is_valid_value(value)
        if value <= 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    @staticmethod
    def _is_valid_value(value):
        super()._is_valid_value(value)
        if value <= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(2),
          PrimeNumber(5),
          PrimeNumber(19),
          FloatPositive(5.4),
          FloatPositive(15.3),
          FloatPositive(11.5),
          FloatPositive(2.4),
          FloatPositive(0.5)
          ]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))