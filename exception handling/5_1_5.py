class Validator:
    _TYPE = None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value, *args, **kwargs):
        if type(value) != self._TYPE or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    _TYPE = float


class IntegerValidator(Validator):
    _TYPE = int


def is_valid(lst, validators):
    least_any_valid = []
    for elem in lst:
        for validator in validators:
            try:
                validator(elem)
                least_any_valid.append(elem)
            except ValueError:
                pass
    return least_any_valid


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]

print(lst_out)
