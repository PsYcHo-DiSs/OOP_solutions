class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if any(type(x) not in (int, float) for x in (self.a, self.b, self.c)) or any(
                num <= 0 for num in (self.a, self.b, self.c)):
            return 1
        if (self.a + self.b < self.c) or (self.b + self.c < self.a) or (self.a + self.c < self.b):
            return 2
        return 3


a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
