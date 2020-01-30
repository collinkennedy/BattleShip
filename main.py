from typing import Iterable, Set, Tuple, Dict, List
import sys
from game_class import Game
from player_class import Player
from board_class import Board
from ship_class import Ship

if __name__ == '__main__':
    boardDims : Iterable[List] = [6,6]
    game = Game(boardDims[0], boardDims[1], '*', 5)
    game.play()