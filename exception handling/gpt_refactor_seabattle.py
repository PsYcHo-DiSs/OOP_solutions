from random import randint
from copy import deepcopy
import numpy as np


class TryToMoveAnotherDirectionError(Exception):
    """Ошибка при попытке движения в недопустимом направлении"""
    pass


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        """
        Инициализация корабля с заданной длиной, типом (ориентацией) и координатами.

        :param length: Длина корабля (количество палуб).
        :param tp: Ориентация корабля (1 - горизонтальная, 2 - вертикальная).
        :param x: Начальная координата X.
        :param y: Начальная координата Y.
        """
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True

        # 1 - попадания не было, 2 - попадание в соответствующую палубу
        self._cells = [1 for _ in range(self._length)]

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом")

        if 0 <= item < len(self._cells):
            return self._cells[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        self._cells[key] = value

    def set_start_coords(self, x, y):
        """Устанавливает начальные координаты корабля."""
        self._x = x
        self._y = y

    def get_start_coords(self):
        """Возвращает начальные координаты корабля (x, y)."""
        return self._x, self._y

    @property
    def orientation(self):
        """Возвращает ориентацию корабля."""
        return self._tp

    @property
    def length(self):
        """Возвращает длину корабля (количество палуб)."""
        return self._length

    @property
    def get_decks(self):
        """Возвращает список состояния палуб корабля."""
        return self._cells

    def can_move(self):
        """Проверяет, может ли корабль двигаться."""
        if any(deck != 1 for deck in self._cells):
            self._is_move = False
        return self._is_move

    def move(self, go):
        """Перемещает корабль на одну клетку, если движение возможно.

        :param go: Направление движения (1 - вперед, -1 - назад).
        :return: Новый объект корабля, если движение допустимо, иначе текущий объект.
        """
        if self.can_move():
            test_ship = deepcopy(self)
            if self.orientation == 1:  # Горизонтальная ориентация
                test_ship._x += go
                if not test_ship.is_out_pole():
                    return test_ship
            elif self.orientation == 2:  # Вертикальная ориентация
                test_ship._y += go
                if not test_ship.is_out_pole():
                    return test_ship
        return self

    def is_collide(self, other: "Ship") -> bool:
        """Проверяет, пересекается ли текущий корабль с другим кораблем.

        :param other: Другой корабль для проверки на столкновение.
        :return: True, если корабли пересекаются, иначе False.
        """
        ship_cells = self._get_ship_cells()
        collision_zone = self._get_collision_zone(ship_cells)
        other_cells = other._get_ship_cells()
        return not collision_zone.isdisjoint(other_cells)

    def _get_ship_cells(self):
        """Возвращает клетки, занимаемые кораблем."""
        return {(self._x + i, self._y) if self.orientation == 1 else (self._x, self._y + i) for i in range(self.length)}

    def _get_collision_zone(self, ship_cells):
        """Возвращает зону возможного столкновения вокруг корабля."""
        collision_zone = set()
        for x, y in ship_cells:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    collision_zone.add((x + dx, y + dy))
        return collision_zone

    def is_out_pole(self, size=10):
        """Проверяет, выходит ли корабль за пределы игрового поля.

        :param size: Размер игрового поля.
        :return: True, если выходит за пределы поля, иначе False.
        """
        if self.orientation == 1:  # Горизонтальная ориентация
            right_end = self._x + self._length - 1
            return not 0 <= right_end < size
        if self.orientation == 2:  # Вертикальная ориентация
            top_end = self._y + self._length - 1
            return not 0 <= top_end < size
        return False


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []
        self._field = np.zeros((size, size), dtype=int)

    def init(self):
        """Начальная инициализация игрового поля, размещение кораблей на поле."""
        for deck, qty in zip(range(4, 0, -1), range(1, 5)):
            self._ships += [Ship(deck, tp=randint(1, 2)) for _ in range(qty)]

        ships_with_coords = []
        for indx, ship in enumerate(self._ships):
            self._place_ship_randomly(ship, ships_with_coords, indx)
        self._ships = deepcopy(ships_with_coords)
        self.set_field()

    def _place_ship_randomly(self, ship, ships_with_coords, indx):
        """Размещает корабль на поле случайным образом, проверяя на пересечения."""
        while True:
            x, y = randint(0, self._size - 1), randint(0, self._size - 1)
            ship.set_start_coords(x, y)
            if not ship.is_out_pole(self._size) and not any(ship.is_collide(s) for s in ships_with_coords):
                ships_with_coords.append(ship)
                break

    def move_ships(self):
        """Перемещает корабли случайным образом вперед или назад."""
        for ship in self._ships:
            try:
                target = ship.move(1)
                if ship.get_start_coords() == target.get_start_coords():
                    raise TryToMoveAnotherDirectionError
            except TryToMoveAnotherDirectionError:
                ship.move(-1)

    def show(self):
        """Отображает игровое поле в консоли."""
        letters = 'abcdefghij'[:self._size]
        digits = list(range(1, self._size + 1))
        print('  ', letters.upper())
        for r in range(self._size):
            print(f'{digits[r]:2}', end=' ')
            for c in range(self._size):
                print(self._field[r, c], end=' ')
            print()

    def set_field(self):
        """Обновляет игровое поле с учетом расположения кораблей."""
        for ship in self._ships:
            if ship.orientation == 1:  # Горизонтальная ориентация
                target_row = ship.get_start_coords()[1]
                self._field[target_row, ship._x: ship._x + ship.length] = ship.get_decks()
            elif ship.orientation == 2:  # Вертикальная ориентация
                target_col = ship.get_start_coords()[0]
                self._field[ship._y: ship._y + ship.length, target_col] = ship.get_decks()

    def get_pole(self):
        """Возвращает текущее состояние игрового поля в виде кортежа."""
        return tuple(tuple(row) for row in self._field)
