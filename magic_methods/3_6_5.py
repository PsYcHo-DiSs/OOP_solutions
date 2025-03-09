s_inp = input()  # эту строку (переменную s_inp) в программе не менять


class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key == 'a' or key == 'b' or key == 'c':
            if type(value) in (int, float):
                if not value > 0:
                    raise ValueError("габаритные размеры должны быть положительными числами")
                else:
                    object.__setattr__(self, key, value)
            else:
                object.__setattr__(self, key, None)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


lst_dims = [Dimensions(*map(float, elem.split())) for elem in s_inp.split('; ')]
lst_dims.sort(key=hash)
