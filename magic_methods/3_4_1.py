class NewList:
    def __init__(self, lst=None):
        if lst is None:
            self._lst = list()
        else:
            self._lst = lst[:]

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError("Правый операнд должен быть типом list или объектом класс NewList")
        deductible_lst = other if type(other) == list else other.get_list()
        return NewList(self.remove_elements(self._lst, deductible_lst))

    def __rsub__(self, other):
        if isinstance(other, list):
            return NewList(self.remove_elements(other, self._lst))
        else:
            raise ArithmeticError("Правый операнд должен быть типом list")

    def get_list(self):
        return self._lst

    @staticmethod
    def remove_elements(lst_1, lst_2):
        typed_lst_1 = list((x, type(x)) for x in lst_1)
        typed_lst_2 = list((x, type(x)) for x in lst_2)
        for elem in typed_lst_2:
            if elem in typed_lst_1:
                typed_lst_1.remove(elem)

        return list(elem[0] for elem in typed_lst_1)


'''
class NewList:
    def __init__(self, lst=None):
        if lst is None:
            self._lst = list()
        else:
            self._lst = lst[:]

    def get_list(self):
        return self._lst

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError("Правый операнд должен быть типом list или объектом класс NewList")

        deductible_lst = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst, deductible_lst))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError("Правый операнд должен быть типом list")

        return NewList(self.__diff_list(other, self._lst))

    @staticmethod
    def __diff_list(lst_1, lst_2):
        if len(lst_2) == 0:
            return lst_1
        sub = lst_2[:]
        return [x for x in lst_1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res
'''