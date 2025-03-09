class Clock:
    @classmethod
    def __check_time(cls, tm):
        if type(tm) == int:
            if 0 <= tm < 100_000:
                return True
        return False

    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if Clock.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


clock = Clock(4530)
print(clock.get_time())
