class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    __rng_rating = range(6)

    def __init__(self, rating=0):
        self.rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating_validator(value)
        self.__rating = value

    @classmethod
    def __rating_validator(cls, value):
        if value not in cls.__rng_rating:
            raise ValueError('неверное присваиваемое значение')

