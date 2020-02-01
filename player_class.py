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
        self.hitCounter = 0
        self.listOfPlayerShips : List[Ship] = []  # contains all the Ship objects read in from the configuration file
        self.overlappingShips : List[Ship.getShipName[0]] = []

    def getListOfShips(self):
        """
        loop through the dictionary that is returned by the
        readFileShips() method in the Ship class, and create ship objects
        and append those ship objects to the listOfPlayerShips attribute 
        of the Player class (which is a list)
        """
        returnedDictOfShips = Ship.readFileShips()
        for shipName, shipSize in returnedDictOfShips.items(): # create a ship object with those attributes and store it in a list
            newShip = Ship(shipName, shipSize)
            self.listOfPlayerShips.append(newShip)
        print(self.listOfPlayerShips)
        return self.listOfPlayerShips

    def move(self, curPlayer : "Player", otherPlayer : "Player"):
        while True:
            try:
                enteredX, enteredY = input(f"{curPlayer.name}, please enter a coordinate to fire upon: ").split(',')
                x, y = int(enteredX), int(enteredY)
                break
            except ValueError:
                print("Your firing position is invalid.")
        begin = True
        while begin:
            try:
                while (curPlayer.scanningBoard.contents[x][y] != curPlayer.scanningBoard.blankChar):
                    enteredX, enteredY = input(f"{curPlayer.name}, please enter a coordinate that has NOT been previously fired upon: ").split(',')
                    x, y = int(enteredX), int(enteredY)
                curPlayer.fire(otherPlayer, x, y)
                begin = False
            except IndexError:
                enteredX, enteredY = input(f"{curPlayer.name}, please enter a coordinate that is on the board: ").split(',')
                x, y = int(enteredX), int(enteredY)
            except ValueError:
                print("Your firing position is invalid.")

    def fire(self, otherPlayer : "Player", x : int, y : int):
        if otherPlayer.playerBoard.contents[x][y] == otherPlayer.playerBoard.blankChar:
            self.scanningBoard.contents[x][y] = 'M'
            print(f"You missed, {self.name}. xD")
        else:
            temp = otherPlayer.playerBoard.contents[x][y]
            self.scanningBoard.contents[x][y] = 'X'
            otherPlayer.playerBoard.contents[x][y] = 'X'
            print(f"You hit a ship, {self.name}. :/")
            for i in otherPlayer.playerBoard.lettersOnBoard:
                if otherPlayer.playerBoard.lettersOnBoard[i] == temp:
                    del otherPlayer.playerBoard.lettersOnBoard[i]
                    break
                else:
                    print(f"You destroyed")
            self.hitCounter += 1
        pass

    @staticmethod
    def getNameFromPlayer(otherPlayers: Iterable["Player"]) -> str:
        alreadyUsedNames = set([player.name for player in otherPlayers])
        while True: # this loops until a player enters a unique name
            name = input('Please enter your name: ')
            if name not in alreadyUsedNames:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def __str__(self) -> str:
        return self.name

if __name__ == "__main__":
    pass