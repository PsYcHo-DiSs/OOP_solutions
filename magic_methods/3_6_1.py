class Rect:
    def __init__(self, x, y, width, height):
        self.x = x if type(x) in (int, float) else None
        self.y = y if type(y) in (int, float) else None
        self.width = width if type(width) in (int, float) else None
        self.height = height if type(height) in (int, float) else None

    def __hash__(self):
        return hash((self.width, self.height))

    def __eq__(self, other):
        if isinstance(other, Rect):
            return self.height == other.height and self.width == other.width
