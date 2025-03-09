from collections import Counter


class Box:
    def __init__(self):
        self._storage_lst = []

    def __eq__(self, other):
        if isinstance(other, Box):
            return self._get_item_counter() == other._get_item_counter()
        return False

    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self._storage_lst.append(obj)

    def get_things(self):
        return self._storage_lst

    def _get_item_counter(self):
        # Создаем счетчик для хранения количества предметов в ящике
        return Counter((thing.name.lower(), thing.mass) for thing in self._storage_lst)


class Thing:
    def __init__(self, name, mass):
        self.name = name if type(name) is str else None
        self.mass = mass if type(mass) in (int, float) else None

    def __eq__(self, other):
        if isinstance(other, Thing):
            return (self.name.lower() == other.name.lower()) and (self.mass == other.mass)
        return False


"""
class Box:
    def __init__(self):
        self._storage_lst = list()

    def __eq__(self, other):
        if isinstance(other, Box):
            if len(self) == len(other):
                self.get_sorted()
                other.get_sorted()
                return self.get_things() == other.get_things()
            return False

    def __len__(self):
        return len(self._storage_lst)

    def get_sorted(self):
        self._storage_lst.sort()

    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self._storage_lst.append(obj)

    def get_things(self):
        return self._storage_lst


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if isinstance(other, Thing):
            return (self.name.lower() == other.name.lower()) and (self.mass == other.mass)

    def __lt__(self, other):
        if isinstance(other, Thing):
            return self.mass < other.mass

    def __le__(self, other):
        if isinstance(other, Thing):
            return self.mass <= other.mass
"""
