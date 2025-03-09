class WordString:
    def __init__(self, string=''):
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        self.__string = string

    def __len__(self):
        return len(self.string.split())

    def words(self, indx):
        return self.string.split()[indx]

    def __call__(self, indx, *args, **kwargs):
        return self.words(indx)
