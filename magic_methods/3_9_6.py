from copy import deepcopy


class Matrix:
    def __init__(self, *args):
        if isinstance(args[0], list):
            self.__is_valid_lst(args[0])
            self.mtrx = deepcopy(args[0])
            self.rows = len(args[0])
            self.cols = len(args[0][0])
        else:
            if len(args) != 3 or not all(type(elem) in (int, float) for elem in args):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

            self.rows = args[0]
            self.cols = args[1]
            self.fill_value = args[2]
            self.mtrx = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]

    @staticmethod
    def __is_valid_lst(lst):
        target = len(lst[0])
        if not all(len(row) == target and all(isinstance(x, (int, float)) for x in row) for row in lst):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __is_valid_indx(self, index):
        r, c = index
        if not (isinstance(r, int) and isinstance(c, int)) or not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('недопустимые значения индексов')

    def __is_valid_value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.rows == other.rows and self.cols == other.cols
        return False

    def __getitem__(self, item):
        self.__is_valid_indx(item)
        r, c = item
        return self.mtrx[r][c]

    def __setitem__(self, key, value):
        self.__is_valid_indx(key)
        self.__is_valid_value(value)
        r, c = key
        self.mtrx[r][c] = value

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self != other:
                raise ValueError('операции возможны только с матрицами равных размеров')
            result = [[self.mtrx[i][j] + other.mtrx[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)
        if isinstance(other, (int, float)):
            result = [[self.mtrx[i][j] + other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self != other:
                raise ValueError('операции возможны только с матрицами равных размеров')
            result = [[self.mtrx[i][j] - other.mtrx[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)
        if isinstance(other, (int, float)):
            result = [[self.mtrx[i][j] - other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)
