class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 if type(x1) in (int, float) else None
        self.y1 = y1 if type(y1) in (int, float) else None
        self.x2 = x2 if type(x2) in (int, float) else None
        self.y2 = y2 if type(y2) in (int, float) else None

    def __len__(self):
        return int((pow((self.x2 - self.x1), 2) + pow((self.y2 - self.x1), 2)) ** 0.5 >= 1)
