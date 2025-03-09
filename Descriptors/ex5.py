class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = list()

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        self.items = [item for item in self.items if item.uid != indx]


class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, new_value):
        self.__id = new_value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_value):
        self.__duration = new_value
