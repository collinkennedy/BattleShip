from typing import Iterable, Set, Tuple, Dict, List
import sys
#from game_class import Game
#from player_class import Player
from board_class import Board
from ship_class import Ship
import game_class

if __name__ == '__main__':
    boardDims : Iterable[List] = [6,6]
    a = 6
    b = 6
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    a = int(line[0])
                    b = int(line[2])
    game = game_class.Game(a, b, '*')
    game.play()