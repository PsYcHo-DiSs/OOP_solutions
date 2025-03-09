class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str:
            if self.min_length <= len(value) <= self.max_length:
                setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float):
            if 0 <= value <= self.max_value:
                setattr(instance, self.name, value)


class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    name = StringValue()

    def __init__(self, name, goods=None):
        self.name = name
        if goods is None:
            self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)
