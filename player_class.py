from typing import Iterable, Set, Tuple, Dict, List
import copy
import sys
import game_class
from board_class import Board
import main
from ship_class import Ship


class Player:
    def __init__(self, otherPlayers: Iterable["Player"], gameBoard: "Board") -> None:
        self.name = self.getNameFromPlayer(otherPlayers)
        self.playerBoard = copy.deepcopy(gameBoard)
        self.scanningBoard = copy.deepcopy(gameBoard)
        self.listOfPlayerShips = []  # contains all the Ship objects read in from the configuration file

    def getListOfShips(self):
        """loop through the dictionary that is returned by the
        readFileShips() method in the Ship class, and create ship objects
        and append those ship objects to the listOfPlayerShips attribute of the Player class (which is a list)

        """
        returnedDictOfShips = Ship.readFileShips()

        for shipName, shipSize in returnedDictOfShips.items():
            # create a ship object with those attributes and store it in a list
            newShip = Ship(shipName, shipSize)
            self.listOfPlayerShips.append(newShip)

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

    # def takeTurn(self, board : "Board"):
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
