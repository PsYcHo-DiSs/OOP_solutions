from abc import ABC, abstractmethod


class CountryInterface(ABC):

    def get_info(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f'{self._name}: {self._square}, {self._population}'
