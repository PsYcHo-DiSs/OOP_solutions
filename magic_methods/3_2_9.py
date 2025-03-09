class RenderDigit:
    def __call__(self, num, *args, **kwargs):
        try:
            return int(num)
        except ValueError:
            return


class InputValues:
    def __init__(self, render):
        self.__render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))

        return wrapper


render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)
