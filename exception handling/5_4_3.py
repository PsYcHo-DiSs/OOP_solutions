class DateString:
    def __init__(self, date_string):
        d, m, y = self._parse_date(date_string)
        self._validate_date(d, m, y)
        self.DD = d
        self.MM = m
        self.YYYY = y

    def __str__(self):
        return f'{self.DD:02}.{self.MM:02}.{self.YYYY:04}'

    @staticmethod
    def _validate_date(day, month, year):

        calendar_dct = {
            "30_days": {4, 6, 9, 11},
            "31_days": {1, 3, 5, 7, 8, 10, 12}
        }

        if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3000):
            raise DateError("Неверный формат даты")

        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            max_days = 29 if is_leap else 28
            if day > max_days:
                raise DateError("Неверный формат даты")

        if month in calendar_dct["30_days"] and day > 30:
            raise DateError("Неверный формат даты")

    @staticmethod
    def _parse_date(date_value):
        try:
            d, m, y = map(int, date_value.split('.'))
            return d, m, y
        except ValueError:
            raise DateError("Некорректный формат даты. Ожидается DD.MM.YYYY")


class DateError(Exception):
    def __init__(self, text):
        super().__init__(text)


try:
    date_string = input()
    datestring_obj = DateString(date_string)
    print(datestring_obj)

except DateError as e:
    print(e)