import time


class Filter:
    def __init__(self, date: float):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            return
        if type(value) == float and value > 0:
            super().__setattr__(key, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and isinstance(filter, Mechanical):
            self.slot_1 = filter
        elif slot_num == 2 and isinstance(filter, Aragon):
            self.slot_2 = filter
        elif slot_num == 3 and isinstance(filter, Calcium):
            self.slot_3 = filter

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        elif slot_num == 2:
            self.slot_2 = None
        elif slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        if all(slot is not None for slot in (self.slot_1, self.slot_2, self.slot_3), ):
            if all(0 <= (time.time() - slot.date) < self.MAX_DATE_FILTER for slot in
                   (self.slot_1, self.slot_2, self.slot_3), ):
                return True
        return False