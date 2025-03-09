class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__is_valid_dim(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__is_valid_dim(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__is_valid_dim(value):
            self.__c = value

    @classmethod
    def __is_valid_dim(cls, value):
        if isinstance(value, (int, float)):
            return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION
        return False

    def get_capacity(self):
        return self.a * self.b * self.c

    def __gt__(self, other):
        if not isinstance(other, Dimensions):
            raise AttributeError("Сравнивать между собой можно только объекты классов Dimensions")
        return self.get_capacity() > other.get_capacity()

    def __ge__(self, other):
        if not isinstance(other, Dimensions):
            raise AttributeError("Сравнивать между собой можно только объекты классов Dimensions")
        return self.get_capacity() >= other.get_capacity()

    # def __lt__(self, other):
    #     if not isinstance(other, Dimensions):
    #         raise AttributeError("Сравнивать между собой можно только объекты классов Dimensions")
    #     return self.get_capacity() < other.get_capacity()
    #
    # def __le__(self, other):
    #     if not isinstance(other, Dimensions):
    #         raise AttributeError("Сравнивать между собой можно только объекты классов Dimensions")
    #     return self.get_capacity() <= other.get_capacity()


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.get_capacity())

