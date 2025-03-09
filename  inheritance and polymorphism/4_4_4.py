class Aircraft:
    def __init__(self, model, mass, speed, top):
        self.value_is_str(model)
        self._model = model
        self.values_are_positive(mass, speed, top)
        self._mass = mass
        self._speed = speed
        self._top = top

    @staticmethod
    def value_is_str(value):
        if type(value) != str:
            raise TypeError('неверный тип аргумента')

    @staticmethod
    def values_are_positive(*args):
        if any(type(value) not in (int, float) or value <= 0 for value in args):
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self.value_is_int_positive(chairs)
        self._chairs = chairs

    @staticmethod
    def value_is_int_positive(value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError('неверный тип аргумента')


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        if isinstance(weapons, dict):
            for weapon, count in weapons.items():
                self.value_is_str(weapon)
                self.value_is_int_positive(count)
            self._weapons = weapons
        else:
            raise TypeError('неверный тип аргумента')

    @staticmethod
    def value_is_int_positive(value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError('неверный тип аргумента')


planes = [
    PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
    PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
    WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
]