class ListInteger(list):
    def __init__(self, args):
        map(self._is_elem_int, args)
        super().__init__(args)

    def __setitem__(self, key, value):
        self._is_elem_int(value)
        super().__setitem__(key, value)

    @staticmethod
    def _is_elem_int(elem):
        if type(elem) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def append(self, elem):
        self._is_elem_int(elem)
        super().append(elem)
