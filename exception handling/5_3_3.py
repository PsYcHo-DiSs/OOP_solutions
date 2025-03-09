class Test:
    _min_len = 10
    _max_len = 10_000

    def __init__(self, descr):
        self._is_valid_descr(descr)
        self.descr = descr

    def _is_valid_descr(self, s_value):
        if not (self._min_len <= len(s_value) <= self._max_len):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')

        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        try:
            ans = float(input())
        except ValueError:
            return False
        else:
            return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


descr, ans = map(str.strip, input().split('|'))
try:
    testAnsDigit = TestAnsDigit(descr, float(ans))
    print(testAnsDigit.run())
except Exception as e:
    print(e)
