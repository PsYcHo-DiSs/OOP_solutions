import sys


class DataBase:
    def __init__(self, path):
        self.path = path if type(path) == str else None
        self.dict_db = dict()

    def write(self, record):
        if isinstance(record, Record):
            self.dict_db.setdefault(record, []).append(record)

    def read(self, pk):
        for key in self.dict_db.values():
            if len(key) == 1 and key[0].pk == pk:
                return key[0]
            else:
                for value in key:
                    if value.pk == pk:
                        return value


class Record:
    PK = 0

    def __new__(cls, *args, **kwargs):
        cls.PK += 1
        return super().__new__(cls)

    def __init__(self, fio, descr, old):
        cls = self.__class__
        self.pk = cls.PK
        self.fio = fio if type(fio) == str else None
        self.descr = descr if type(descr) == str else None
        self.old = old if type(old) == int else None

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        if not isinstance(other, Record):
            raise AttributeError("Сравнению между собой подлежат только обьекты класса Record")
        return (self.fio == other.fio) and (self.old == other.old)


lst_in = list(map(str.strip, sys.stdin.readlines()))
db = DataBase('path')
for i in lst_in:
    text = i.split('; ')
    record = Record(text[0].strip(), text[1].strip(), int(text[2].strip()))
    db.write(record)
