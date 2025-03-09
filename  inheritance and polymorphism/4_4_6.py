CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


# здесь объявляйте класс FileDialogFactory
class FileDialogFactory:
    def __new__(cls, title, path, exts):
        if CURRENT_OS == 'windows':
            instance = super().__new__(WindowsFileDialog)
            instance.__init__(title, path, exts)
        else:
            instance = super().__new__(LinuxFileDialog)
            instance.__init__(title, path, exts)

        return instance


    @staticmethod
    def create_windows_filedialog(title, path, exts):
        pass

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        pass

