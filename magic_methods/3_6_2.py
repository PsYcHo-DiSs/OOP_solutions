import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name if type(name) == str else None
        self.weight = weight if type(weight) in (int, float) else None
        self.price = price if type(price) in (int, float) else None

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        if not isinstance(other, ShopItem):
            raise AttributeError("Сравнению между собой подлежат только обьекты класса ShopItem")
        return (self.name == other.name) and (self.weight == other.weight) and (self.price == other.price)



lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!

shop_items = {}
for i in lst_in:
    n = i.split(":")[0]
    w = float(i.split(":")[1].split()[0])
    p = float(i.split(":")[1].split()[1])
    total = 1
    obj = ShopItem(n, w, p)
    if obj in shop_items:
        shop_items[obj][1] += 1
    else:
        shop_items[obj] = [obj, total]
