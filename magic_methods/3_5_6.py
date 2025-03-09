class Money:
    money_type = None
    EPS = 0.1

    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None
        self.__in_rubls = 0

    def __eq__(self, other):
        if self.__is_wallet_valid(other):
            return abs(self.__in_rubls - other.__in_rubls) <= self.EPS

    def __lt__(self, other):
        if self.__is_wallet_valid(other):
            return self.__in_rubls < other.__in_rubls

    def __le__(self, other):
        if self.__is_wallet_valid(other):
            return self.__in_rubls <= other.__in_rubls

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, obj):
        self.__cb = obj

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __is_wallet_valid(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        self.convert_to_rubls()
        other.convert_to_rubls()
        return True

    def convert_to_rubls(self):
        if self.cb and self.money_type:
            base_to_rub = self.cb.rates['rub'] / self.cb.rates[self.money_type]
            self.__in_rubls = self.__volume * base_to_rub
        else:
            self.__in_rubls = self.__volume


class MoneyR(Money):
    money_type = 'rub'


class MoneyD(Money):
    money_type = 'dollar'


class MoneyE(Money):
    money_type = 'euro'


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        pass

    @classmethod
    def register(cls, money):
        if isinstance(money, Money):
            money.cb = cls

