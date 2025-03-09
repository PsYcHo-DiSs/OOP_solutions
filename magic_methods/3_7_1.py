import sys


class Player:
    def __init__(self, name, old, score):
        self.name = name if type(name) == str else None
        self.old = old if type(old) == int else None
        self.score = score if type(score) == int else None

    def __bool__(self):
        return bool(self.score)


lst_in = list(map(str.strip, sys.stdin.readlines()))

players = [Player(elem.split('; ')[0], int(elem.split('; ')[1]), int(elem.split('; ')[2])) for elem in lst_in]
players_filtered = list(filter(bool, players))