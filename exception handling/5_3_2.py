class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if type(string) != str:
            raise ValueError('недопустимая строка')
        if not (self.min_length <= len(string) <= self.max_length):
            raise ValueError('недопустимая строка')

        if self.chars:
            if not len(set(string) & set(self.chars)) >= 1:
                raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = None
        self._password = None

    def form(self, request):
        try:
            login = request['login']
            password = request['password']
        except KeyError:
            raise TypeError('в запросе отсутствует логин или пароль')

        self.login_validator.is_valid(login)
        self.password_validator.is_valid(password)

        self._login = login
        self._password = password
