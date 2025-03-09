class StringDigit(str):
    def __init__(self, string):
        self.string = string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self.__is_value_valid(value)
        self._string = value

    @staticmethod
    def __is_value_valid(value):
        if type(value) != str:
            raise TypeError("передаваемая на вход последовательность должна принадлежать к типу str")
        if not value.isdigit():
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        self.__is_value_valid(other)
        return StringDigit(self.string + other)

    def __radd__(self, other):
        self.__is_value_valid(other)
        return StringDigit(other + self.string)
