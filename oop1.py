import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False

        for attr, value in zip(fields, lst_values):
            setattr(self, attr, value)
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


# Пример использования:
# В платформе или через консоль:
# sr = StreamReader()
# data, result = sr.readlines()

# В случае тестирования локально, можно использовать следующий код:
if __name__ == "__main__":
    import io

    sys.stdin = io.StringIO("10\nПитон - основы мастерства\n512\n")
    sr = StreamReader()
    data, result = sr.readlines()
    print(data.__dict__)  # {'id': '10', 'title': 'Питон - основы мастерства', 'pages': '512'}
    print(result)  # True
