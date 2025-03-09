class AppVK:
    def __init__(self, name):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list


class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = list()

    def add_app(self, app):
        if app not in self.apps:
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)
