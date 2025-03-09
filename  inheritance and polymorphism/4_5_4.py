from abc import ABC, abstractmethod


# здесь объявляйте классы
class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return f'Базовый класс Model'


class ModelForm(Model):
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = hash(self)

    def get_pk(self):
        return self._id
