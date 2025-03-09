class AppStore:
    __instance = None
    applications = list()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance

    @classmethod
    def add_application(cls, app):
        cls.applications.append(app)

    @classmethod
    def remove_application(cls, app):
        cls.applications.remove(app)

    @classmethod
    def block_application(cls, app):
        setattr(cls.applications[cls.applications.index(app)], 'blocked', True)

    @classmethod
    def total_apps(cls):
        return len(cls.applications)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked
