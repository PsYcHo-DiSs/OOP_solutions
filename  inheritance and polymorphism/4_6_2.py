class ShopGenericView:
    def __repr__(self):
        return "\n".join([f'{attr}: {value}' for attr, value in self.__dict__.items()])


class ShopUserView:
    def __str__(self):
        return "\n".join([f'{attr}: {value}' for attr, value in self.__dict__.items() if attr != '_id'])


class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView

class Book(ShopItem, ShopGenericView, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year
