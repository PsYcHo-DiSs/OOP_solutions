class Track:
    def __init__(self, start_x, start_y):
        self.start = (start_x, start_y)
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append(((x, y), speed))

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self.points):
            return self.points[index]
        else:
            raise IndexError('некорректный индекс')

    def __setitem__(self, index, value):
        if isinstance(index, int) and 0 <= index < len(self.points):
            coord = self.points[index][0]
            self.points[index] = (coord, value)
        else:
            raise IndexError('некорректный индекс')
