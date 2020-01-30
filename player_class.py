from typing import Iterable, Set, Tuple, Dict, List
import copy
import sys
import game_class
from board_class import Board
import main
#from ship_class import Ship


class Player:
    def __init__(self, otherPlayers: Iterable["Player"], gameBoard : "Board") -> None:
        self.name = self.getNameFromPlayer(otherPlayers)
        self.playerBoard = copy.deepcopy(gameBoard)

    @staticmethod
    def getNameFromPlayer(otherPlayers: Iterable["Player"]) -> str:
        """get a VALID name form the player.
        A name that is already used is invalid!!!
        """
        alreadyUsedNames = set([player.name for player in otherPlayers])
        while True:
            name = input('Please enter your name: ')
            if name not in alreadyUsedNames:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def __str__(self) -> str:
        return self.name

    #def takeTurn(self, board : "Board"):
    #    x = 1
    #    if x == 1:
    #        #set up game
    #        self.playerBoard = copy.deepcopy(board)
    #        self.playerBoard.findLocation(3,4)
    #        print(self.playerBoard)
    #        x = 2
    #    else:
    #        #take regular turn
    #        pass
    #    pass


if __name__ == "__main__":
    pass
