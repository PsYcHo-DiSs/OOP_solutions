class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = list()

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if thing.weight + self.get_total_weight() <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum(t.weight for t in self.__things)


class Thing:
    def __init__(self, name, weight):
        if type(name) == str:
            self.name = name
        if type(weight) in (int, float):
            self.weight = weight
