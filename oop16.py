class Viber:
    __instance = None
    messages = list()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance

    @classmethod
    def add_message(cls, msg):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.messages.remove(msg)

    @classmethod
    def set_like(cls, msg):
        has_like = getattr(cls.messages[cls.messages.index(msg)], 'fl_like')
        if not has_like:
            setattr(cls.messages[cls.messages.index(msg)], 'fl_like', True)
        else:
            setattr(cls.messages[cls.messages.index(msg)], 'fl_like', False)

    @classmethod
    def show_last_message(cls, number):
        return cls.messages[-number:]

    @classmethod
    def total_messages(cls):
        return len(cls.messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like
