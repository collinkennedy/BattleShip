from typing import Iterable, Set, Tuple, Dict, List
import copy
import sys
import game_class
from board_class import Board
import main
from ship_class import Ship

class AIPlayer:
    def __init__(self, otherPlayers: Iterable["Player"], gameBoard: "Board") -> None:
        pass

    def __str__(self) -> str:
        return self.name

    def getListOfShips(self):
        pass

    def move(self, curPlayer : "Player", otherPlayer : "Player"):
        pass

    def fire(self, otherPlayer : "Player", x : int, y : int):
        pass

    @staticmethod
    def getNameFromPlayer(otherPlayers: Iterable["Player"]) -> str:
        pass
    
if __name__ == "__main__":
    pass