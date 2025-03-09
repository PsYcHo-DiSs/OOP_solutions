class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id_cls = 0

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__dict__['id'] = cls.id_cls
        cls.id_cls += 1
        return instance

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'name' and isinstance(value, str):
            super().__setattr__(key, value)
        elif key in {'weight', 'price'} and isinstance(value, (int, float)) and value > 0:
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            super().__delattr__(item)
