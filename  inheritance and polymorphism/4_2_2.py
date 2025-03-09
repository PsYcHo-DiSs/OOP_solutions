class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __eq__(self, other):
        if isinstance(other, Thing):
            return hash(self) == hash(other)
        return False


class DictShop(dict):
    def __new__(cls, *args, **kwargs):
        for k in kwargs.keys():
            cls._is_key_valid(k)
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, things=None):
        if things is None:
            things = dict()
        if not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')
        for k in things.keys():
            self._is_key_valid(k)
        super().__init__(things)

    def __setitem__(self, key, value):
        self._is_key_valid(key)
        super().__setitem__(key, value)

    @staticmethod
    def _is_key_valid(key):
        if type(key) != Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')

