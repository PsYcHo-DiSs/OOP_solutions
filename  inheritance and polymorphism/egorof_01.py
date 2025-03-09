class MaxLengthAttribute:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return max(instance.__dict__.keys(), key=lambda x: (len, x), default=None)