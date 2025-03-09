from random import randint
from copy import deepcopy
import numpy as np


class TryToMoveAnotherDirectionError(Exception):
    pass


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True

        # 1 - попадания не было
        # 2 - попадание в соответствующую палубу
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
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    @property
    def orientation(self):
        return self._tp

    @property
    def length(self):
        return self._length

    @property
    def get_decks(self):
        return self._cells

    def can_move(self):
        '''Если одна из палуб не равна 1,
           корабль теряет способность к перемещению'''
        if any(deck != 1 for deck in self._cells):
            self._is_move = False
        return self._is_move

    def move(self, go):
        '''Возвращает новый объект класса ship
        если движение валидно, или старый объект если невалидно'''
        # go это (1 / -1)
        if self.can_move():  # если корабль может двигаться
            test_ship = deepcopy(self)
            if self.orientation == 1:
                '''горизонтальная ориентация, 
                   значит двигаемся по неизменной оси y'''
                if go > 0:
                    # движение вправо -> увеличиваем self._x += 1
                    test_ship._x += 1
                    if not test_ship.is_out_pole():
                        '''если корабль с измененной координатой
                        в пределах поля, то сохраняем результат движения'''
                        return test_ship
                    else:
                        # иначе, остаёмся на месте, значит возвращаем старый объект.
                        return self
                if go < 0:
                    # движение влево <- уменьшаем self._x -= 1
                    test_ship._x -= 1
                    if not test_ship.is_out_pole():
                        '''если корабль с измененной координатой
                        в пределах поля, то сохраняем результат движения'''
                        return test_ship
                    else:
                        # иначе, остаёмся на месте, значит возвращаем старый объект.
                        return self

            elif self.orientation == 2:  # вертикальная ориентация
                '''вертикальная ориентация, 
                   значит двигаемся по неизменной оси x'''
                if go > 0:
                    # движение вниз -> увеличиваем self._y += 1
                    test_ship._y += 1
                    if not test_ship.is_out_pole():
                        '''если корабль с измененной координатой
                        в пределах поля, то сохраняем результат движения'''
                        return test_ship
                    else:
                        # иначе, остаёмся на месте, значит возвращаем старый объект.
                        return self
                if go < 0:
                    # движение вверх <- уменьшаем self._y -= 1
                    test_ship._y -= 1
                    if not test_ship.is_out_pole():
                        '''если корабль с измененной координатой
                        в пределах поля, то сохраняем результат движения'''
                        return test_ship
                    else:
                        # иначе, остаёмся на месте, значит возвращаем старый объект.
                        return self
        else:  # корабль не мог двигаться, остаёмся на месте
            return self

    def is_collide(self, other: "Ship") -> bool:
        """ Проверяет, пересекается ли данный корабль с другим,
            включая граничные клетки вокруг него.
        """
        # Получаем клетки текущего корабля
        ship_cells = {(self._x + i, self._y) if self.orientation == 1 else (self._x, self._y + i) for i in
                      range(self.length)}

        # Формируем зону вокруг корабля (включая его самого)
        collision_zone = set()
        for x, y in ship_cells:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    collision_zone.add((x + dx, y + dy))

        # Получаем клетки другого корабля
        other_x, other_y = other.get_start_coords()
        other_cells = {(other_x + i, other_y) if other.orientation == 1 else (other_x, other_y + i) for i in
                       range(other.length)}

        # Проверяем пересечение зон
        return not collision_zone.isdisjoint(other_cells)

    def is_out_pole(self, size=10):
        '''Проверка на выход корабля за пределы игрового поля '''
        # return true / False
        if self.orientation == 1:  # горизонтальная ориентация
            '''нужна универсальная формула для просчёта диапазона допустимости 
            в зависимоти от палубности корабля'''
            # (сама точка начала (x, y) + self._length - 1)
            # должно укладывать своё тело в диапазоне [0 до size - 1]
            left_end = self._x
            right_end = left_end + self._length - 1

            if not 0 <= right_end <= size - 1:
                return True

            return False

        if self.orientation == 2:  # вертикальная ориентация
            bottom_end = self._y
            top_end = bottom_end + self._length - 1
            if not 0 <= top_end <= size - 1:
                return True

            return False


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []
        self._field = np.zeros((size, size), dtype=int)

    def init(self):
        '''Начальная инициализация игрового поля;
        здесь создается список из кораблей (объектов класса Ship):
        однопалубных - 4;
        двухпалубных - 3;
        трехпалубных - 2;
        четырехпалубный - 1
        (ориентация этих кораблей должна быть случайной).'''

        ''' можно воспользоваться функцией randint
        [Ship(4, tp=randint(1, 2)), 
         Ship(3, tp=randint(1, 2)), 
         Ship(3, tp=randint(1, 2)),
         Ship(2, tp=randint(1, 2)),
         Ship(2, tp=randint(1, 2)), 
         Ship(2, tp=randint(1, 2)),
         Ship(1, tp=randint(1, 2)),
         Ship(1, tp=randint(1, 2)),
         Ship(1, tp=randint(1, 2)),
         Ship(1, tp=randint(1, 2))]'''

        # от бОльших к меньшим
        for deck, qty in zip(range(4, 0, -1), range(1, 5)):
            self._ships += [Ship(deck, tp=randint(1, 2)) for _ in range(qty)]

        '''Начальные координаты x, y не расставленных кораблей равны None.
        После этого, выполняется их расстановка на игровом поле 
        со случайными координатами так, чтобы корабли 
        не пересекались между собой.'''

        ships_with_coords = []
        for indx, ship in enumerate(self._ships, start=0):
            if indx == 0:  # при начальной итерации имеем дело с 4-х палубником
                while True:
                    x, y = randint(0, self._size - 1), randint(0, self._size - 1)
                    ship.set_start_coords(x, y)  # рандомим начальные координаты
                    if not ship.is_out_pole(self._size):
                        '''так как корабль первый, 
                        проверяем только чтобы он не выходил за пределы поля'''
                        ships_with_coords.append(ship)
                        break
                    else:
                        continue
            else:
                '''вторую и последующие итерации мы должны проверять что каждый
                новый объект класса Ship не пересекается с каждым другим, 
                с уже выданными координатами'''
                while True:
                    x, y = randint(0, self._size - 1), randint(0, self._size - 1)
                    ship.set_start_coords(x, y)
                    if not ship.is_out_pole(self._size):
                        if any(ship.is_collide(s) for s in ships_with_coords):
                            '''если есть пересечение хоть с одним кораблём, 
                            нам такие кооррдинаты не подходят => рандомим дальше'''
                            continue
                        else:
                            '''иначе корабль отправляется в список объектов, 
                            с устоявшимися координатами'''
                            ships_with_coords.append(ship)
                            break

        self._ships.clear()
        self._ships = deepcopy(ships_with_coords)
        self.set_field()

    def get_ships(self):
        return self._ships

    def move_ships(self):
        ''' Перемещает каждый корабль из коллекции _ships
        на одну клетку (случайным образом вперед или назад)
        в направлении ориентации корабля;
        если перемещение в выбранную сторону невозможно
        (другой корабль или пределы игрового поля),
        то попытаться переместиться в противоположную сторону,
        иначе (если перемещения невозможны), оставаться на месте;'''
        for ship in self._ships:
            try:
                target = ship.move(1)
                if ship.get_start_coords() == target.get_start_coords():
                    raise TryToMoveAnotherDirectionError
            except TryToMoveAnotherDirectionError:
                ship.move(-1)

    def show(self):
        '''
        Отображение игрового поля в консоли
        (корабли должны отображаться значениями из коллекции _cells
        каждого корабля, вода - значением 0);
        '''
        letters = 'abcdefghij'[:self._size]
        digits = list(range(1, self._size + 1))  # Числа от 1 до 10

        print('  ', letters.upper())
        # Вывод игрового поля
        for r in range(self._size):
            print(f'{digits[r]:2}', end=' ')  # Числовой индекс с выравниванием
            for c in range(self._size):
                print(self._field[r, c], end=' ')
            print()  # Перенос строки

    def set_field(self):
        for ship in self._ships:
            # get_start_coords возвращает self._x, self._y
            # строка - y, колонка - x
            if ship.orientation == 1:
                # горизонтальная
                target_row = ship.get_start_coords()[1]
                left_end_idx = ship.get_start_coords()[0]
                right_end_idx = left_end_idx + len(ship.get_decks)
                # если ориентация горизонтальная, target_row не меняется
                self._field[target_row, left_end_idx: right_end_idx] = ship.get_decks

            elif ship.orientation == 2:
                # вертикальная
                target_col = ship.get_start_coords()[0]
                bottom_end_idx = ship.get_start_coords()[1]
                top_end_idx = bottom_end_idx + len(ship.get_decks)
                # если ориентация вертикальная, target_col не меняется
                self._field[bottom_end_idx: top_end_idx, target_col] = ship.get_decks

    def get_pole(self):
        '''Получение текущего игрового поля в виде двумерного (вложенного) кортежа.'''
        return tuple(tuple(row) for row in self._field)
