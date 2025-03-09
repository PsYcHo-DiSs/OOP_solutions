class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if not isinstance(other, Item) or not isinstance(other.money, (int, float)):
            raise AttributeError("Неправильный тип данных")
        self.money += other.money
        return self.money

    def __radd__(self, other):
        return other + self.money


class Budget:
    def __init__(self):
        self.expenditure_items = list()

    def add_item(self, it):
        self.__is_valid_item(it)
        self.expenditure_items.append(it)

    def remove_item(self, indx):
        self.expenditure_items.pop(indx)

    def get_items(self):
        return self.expenditure_items

    @staticmethod
    def __is_valid_item(item):
        if not isinstance(item, Item):
            raise TypeError("Добавлять возможно только объекты класса Item")
