class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if (key == 'title' or key == 'author') and type(value) == str:
            super().__setattr__(key, value)
        elif (key == 'pages' or key == 'year') and type(value) == int:
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)