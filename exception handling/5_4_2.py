class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if not kwargs:
            self.message = f'Первичный ключ должен быть целым неотрицательным числом'
        else:
            key, value = next(iter(kwargs.items()))
            self.message = f'Значение первичного ключа {key} = {value} недопустимо'

    def __str__(self):
        return self.message


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
