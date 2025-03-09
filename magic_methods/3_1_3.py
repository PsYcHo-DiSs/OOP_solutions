class LessonItem:

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title' and isinstance(value, str):
            super().__setattr__(key, value)
        elif key in {'practices', 'duration'} and isinstance(value, int) and value > 0:
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item not in {'title', 'practices', 'duration'}:
            super().__delattr__(item)
        else:
            raise AttributeError(f"Атрибут {item} удалять запрещено.")


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = list()

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = list()

    def add_module(self, modules):
        self.modules.append(modules)

    def remove_module(self, indx):
        self.modules.pop(indx)


"""
class LessonItem:
    __attr = {
        'title': lambda value: isinstance(value, str),
        'practices': lambda value: isinstance(value, int) and value > 0,
        'duration': lambda value: isinstance(value, int) and value > 0
    }

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.__attr and not self.__attr[key](value):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)
"""