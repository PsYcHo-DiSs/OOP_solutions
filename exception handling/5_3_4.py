# здесь объявляйте класс
class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __repr__(self):
        return ' '.join(map(str, self))


digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

# здесь создавайте объект класса
try:
    obj = TupleLimit(digits, 5)
    print(obj)
except ValueError as e:
    print(e)
