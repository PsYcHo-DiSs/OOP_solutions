class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.fields = list(kwargs.keys())

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self.fields):
            return getattr(self, self.fields[index])
        else:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, index, value):
        if isinstance(index, int) and 0 <= index < len(self.fields):
            setattr(self, self.fields[index], value)
        else:
            raise IndexError('неверный индекс поля')