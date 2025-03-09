class Food:
    def __init__(self, name, weight, calories):
        self._name = name if type(name) == str else None
        self._weight = weight if type(weight) in (int, float) and weight > 0 else None
        self._calories = calories if type(calories) == int and calories > 0 else None


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self._fish = fish
