class Morph:
    def __init__(self, *words):
        self._word_forms = list(map(lambda x: x.strip(" ?!,.;").lower(), words))

    def __eq__(self, other):
        if isinstance(other, str):
            return other.lower() in self._word_forms
        return False

    def add_word(self, word):
        w = word.lower()
        if w not in self._word_forms:
            self._word_forms.append(w)

    def get_words(self):
        return tuple(self._word_forms)


s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]

text = input()

words_in_text = map(lambda x: x.strip("–?!,.;").lower(), text.split())
res = sum(word == morph for word in words_in_text for morph in dict_words)

print(res)
