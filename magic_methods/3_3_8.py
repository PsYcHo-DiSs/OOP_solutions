class Ingredient:
    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __setattr__(self, key, value):
        if key == 'name' and isinstance(value, str):
            super().__setattr__(key, value)
        elif key == 'volume' and isinstance(value, float):
            super().__setattr__(key, value)
        elif key == 'measure' and isinstance(value, str):
            super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args):
        if not args:
            self.ings = list()
        else:
            self.ings = [*args]

    def __len__(self):
        return len(self.ings)

    def add_ingredient(self, ing):
        self.ings.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.ings:
            self.ings.remove(ing)

    def get_ingredients(self):
        return self.ings
