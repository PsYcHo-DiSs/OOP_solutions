class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width if self.__is_correct_num(width) else 0
        self.__height = height if self.__is_correct_num(height) else 0

    @staticmethod
    def __is_correct_num(num):
        return isinstance(num, int) and 0 <= num <= 10000

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.__is_correct_num(width) and self.__width != width:
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__is_correct_num(height) and self.__height != height:
            self.__height = height
            self.show()

    def show(self):
        return f"{self.__title}: {self.__width}, {self.__height}"
