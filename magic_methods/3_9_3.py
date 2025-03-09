class IterColumn:
    def __init__(self, lst, column):
        self._lst = lst
        self.col = column

    def __iter__(self):
        for row in self._lst:
            yield row[self.col]
