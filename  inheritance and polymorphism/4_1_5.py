class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return data


class TypeValidator(Validator):
    data_type = None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, self.data_type) and self.min_value <= data <= self.max_value


class IntegerValidator(TypeValidator):
    data_type = int


class FloatValidator(TypeValidator):
    data_type = float
