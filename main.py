from typing import Iterable, Set, Tuple, Dict, List
import sys
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
                    dimStr = line
                    a, b = int(dimStr.split(" "))
    game = game_class.Game(a, b, '*')
    game.play()