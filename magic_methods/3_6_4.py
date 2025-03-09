import sys


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name if type(name) == str else None
        self.author = author if type(author) == str else None
        self.year = year if type(year) == int else None

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        if not isinstance(other, BookStudy):
            raise AttributeError("Сравнению между собой подлежат только обьекты класса BookStudy")
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_bs = [BookStudy(elem.split('; ')[0], elem.split('; ')[1], int(elem.split('; ')[2])) for elem in lst_in]
unique_books = len(set(lst_bs))
