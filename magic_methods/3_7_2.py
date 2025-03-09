import sys


class MailBox:
    def __init__(self):
        self.inbox_list = list()

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        cls_lst = [MailItem(*elem.split('; ')) for elem in lst_in]
        self.inbox_list.extend(cls_lst)


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from if isinstance(mail_from, str) else None
        self.title = title if isinstance(title, str) else None
        self.content = content if isinstance(content, str) else None
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return bool(self.is_read)


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)

inbox_list_filtered = list(filter(bool, mail.inbox_list))