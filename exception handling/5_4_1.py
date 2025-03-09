class StringException(Exception):
    pass


class NegativeLengthString(StringException):
    """ошибка, если длина отрицательная"""


class ExceedLengthString(StringException):
    """ошибка, если длина превышает заданное значение"""


try:
    raise ExceedLengthString
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")


