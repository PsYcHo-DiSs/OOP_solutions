from functools import reduce


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self._capacity = list()

    def __get_current_weight(self):
        return reduce(lambda total, elem: total + elem.weight, self._capacity, 0)

    def add_thing(self, thing):
        if isinstance(thing, Thing):
            if self.__get_current_weight() + thing.weight <= self.max_weight:
                self._capacity.append(thing)
            else:
                raise ValueError('превышен суммарный вес предметов')

    def __is_valid_index(self, indx):
        if not (type(indx) == int and 0 <= indx < len(self._capacity)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__is_valid_index(item)
        return self._capacity[item]

    def __setitem__(self, key, value):
        self.__is_valid_index(key)
        if isinstance(value, Thing):
            if (self.__get_current_weight() - self._capacity[key].weight + value.weight) <= self.max_weight:
                self._capacity[key] = value
            else:
                raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, key):
        self.__is_valid_index(key)
        del self._capacity[key]


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
