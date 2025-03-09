import time


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        return time.strftime('%H: %M: %S', time.gmtime(self.__len__()))

    def __len__(self):
        delta = self.clock1.get_time() - self.clock2.get_time()
        return max(0, delta)  # Если разница отрицательная, возвращаем 0


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
