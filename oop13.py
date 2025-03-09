from string import ascii_uppercase, digits


class CardCheck:
    CHARS_FOR_NAME = set(ascii_uppercase + digits)
    set_chars = set(CHARS_FOR_NAME)

    @classmethod
    def check_card_number(cls, number):
        if type(number) != str:
            return False
        s = number.split('-')
        if len(s) != 4:
            return False
        if not all(len(num) == 4 for num in s):
            return False
        return all(map(lambda num: num.isdigit(), s))

    @classmethod
    def check_name(cls, name):
        if type(name) != str:
            return False
        s = name.split()
        if len(s) != 2:
            return False
        return all(set(char) < cls.set_chars for char in s)


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
