class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.mass = None

    def __eq__(self, other):
        if type(other) == Body:
            return self.mass == other.mass
        if type(other) in (int, float):
            return self.mass == other

    def __lt__(self, other):
        if type(other) == Body:
            return self.mass < other.mass
        if type(other) in (int, float):
            return self.mass < other

    def __gt__(self, other):
        if type(other) == Body:
            return self.mass > other.mass
        if type(other) in (int, float):
            return self.mass > other

    def get_obj_mass(self):
        self.mass = self.ro * self.volume
        return self.mass
