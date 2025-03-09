class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = list()

    def __add__(self, other):
        self.__is_valid_item(other)
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == int:
            self.book_list.pop(other)
        elif type(other) == Book and other in self.book_list:
            self.book_list.remove(other)
        return self

    def __isub__(self, other):
        return self - other

    def __len__(self):
        return len(self.book_list)

    @staticmethod
    def __is_valid_item(item):
        if not isinstance(item, Book):
            raise TypeError("Добавлять возможно только объекты класса Book")
