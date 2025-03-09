from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        self.__img = img

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            super().__setattr__(key, value)
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return sqrt(self.real * self.real + self.img * self.img)
