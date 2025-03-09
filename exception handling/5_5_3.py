from copy import deepcopy


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []
        self._cur_weight = sum(elem[1] for elem in self._things)

    def add_thing(self, obj):
        if type(obj) != tuple or len(obj) != 2:
            raise TypeError('добавление недопустимого типа данных')

        if self._cur_weight + obj[1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')

        self._cur_weight += obj[1]
        self._things.append(obj)


class BoxDefender:

    def __init__(self, box_obj):
        self.__b = box_obj

    def __enter__(self):
        self.__temp = deepcopy(self.__b)
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__b.__dict__.update(self.__temp.__dict__)
        return False
