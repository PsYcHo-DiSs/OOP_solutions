from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.init()

    def init(self):
        mines_to_place = self.M
        while mines_to_place > 0:
            x, y = randint(0, self.N - 1), randint(0, self.N - 1)
            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                mines_to_place -= 1
                self.update_around_mines(x, y)

    def update_around_mines(self, mine_x, mine_y):
        for i in range(mine_x - 1, mine_x + 2):
            for j in range(mine_y - 1, mine_y + 2):
                if 0 <= i < self.N and 0 <= j < self.N and not self.pole[i][j].mine:
                    self.pole[i][j].around_mines += 1

    def show(self):
        for row in self.pole:
            print(' '.join('#' if not cell.fl_open else '*' if cell.mine else str(cell.around_mines) for cell in row))


pole_game = GamePole(10, 12)
pole_game.show()
