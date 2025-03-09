class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

        self._attribute_names = ['fio', 'job', 'old', 'salary', 'year_job']

    def __is_valid_indx(self, indx):
        if not isinstance(indx, int) or not (0 <= indx < len(self._attribute_names)):
            raise IndexError('неверный индекс')

    def __getitem__(self, indx):
        self.__is_valid_indx(indx)
        attr_name = self._attribute_names[indx]
        return getattr(self, attr_name)

    def __setitem__(self, indx, value):
        self.__is_valid_indx(indx)
        attr_name = self._attribute_names[indx]
        setattr(self, attr_name, value)

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current < len(self._attribute_names):
            attr_name = self._attribute_names[self._current]
            self._current += 1
            return getattr(self, attr_name)
        else:
            raise StopIteration
