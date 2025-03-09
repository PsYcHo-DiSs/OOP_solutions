class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)  # return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)  # instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell(0.0) for _ in range(self.M)] for _ in range(self.N)]


table = TableSheet(5, 3)
n = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = n
        n += 1.0
