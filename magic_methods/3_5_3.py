# эти строчки не менять
stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]


class StringText:
    def __init__(self, lst):
        self.lst_words = list(lst)

    def __len__(self):
        return len(self.lst_words)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


to_delete = "–?!,.;"
lst_text = [StringText(word.strip(to_delete) for word in phrase.split() if len(word.strip(to_delete)) > 0) for phrase in
            stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(elem.lst_words) for elem in lst_text_sorted]