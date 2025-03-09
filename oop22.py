from string import ascii_letters, digits
from random import choice, randrange


class EmailValidator:
    __acceptable = ascii_letters + digits + '_.@'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        username_length = randrange(1, 101)
        username = ''.join(choice(cls.__acceptable[:-3]) for _ in range(username_length))
        return f"{username}@gmail.com"

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if email.count('@') != 1:
            return False
        before_at, after_at = email.split('@')
        if len(before_at) > 100 and len(after_at) > 50:
            return False
        if not all(map(lambda s: s in cls.__acceptable, email)):
            return False
        if '..' in email:
            return False
        if '.' not in after_at:
            return False

        return True

    @staticmethod
    def __is_email_str(email):
        if isinstance(email, str):
            return True
        return False
