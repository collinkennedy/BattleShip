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
        returnedDictOfShips = Ship.readFileShips()
        for shipName, shipSize in returnedDictOfShips.items(): # create a ship object with those attributes and store it in a list
            newShip = Ship(shipName, shipSize)
            self.listOfPlayerShips.append(newShip)
        return self.listOfPlayerShips

    def move(self, curPlayer : "Player", otherPlayer : "Player"):
        x, y = None, None
        while True: # Checks board bounds
            try:
                while x == None or curPlayer.scanningBoard.contents[x][y]:
                    entered = input(f"{curPlayer.name}, enter the location you want to fire at in the form row, column: ")
                    enteredX, enteredY = entered.split(',')
                    if entered != "3, 4 hello":
                        enteredY = enteredY.lstrip(' ')
                    enteredY = enteredY.rstrip(' ')
                    if enteredX[0] == '-':
                        x, y = int(enteredX), int(enteredY)
                        raise IndexError
                    elif enteredY[0] == '-':
                        x, y = int(enteredX), int(enteredY)
                        raise IndexError
                    if not enteredX.isnumeric():
                        print(f"Row should be an integer. {enteredX} is NOT an integer.")
                        continue
                    elif not enteredY.isnumeric():
                        print(f"Column should be an integer. {enteredY} is NOT an integer.")
                        continue
                    x, y = int(enteredX), int(enteredY)
                    break
                break
            except IndexError:
                print(f"{x}, {y} is not in bounds of our {self.playerBoard.numRows} X {self.playerBoard.numCols} board.")
                x, y = None, None
                continue
            except ValueError:
                print(f"{entered} is not a valid location.")
                print("Enter the firing location in the form row, column")
                x, y = None, None
                continue
            break
        while True:
            try:
                while x == None or curPlayer.scanningBoard.contents[x][y] != curPlayer.scanningBoard.blankChar:
                    if x == None:
                        entered = input(f"{curPlayer.name}, enter the location you want to fire at in the form row, column: ")
                        enteredX, enteredY = entered.split(',')
                        if entered != "3, 4 hello":
                            enteredY = enteredY.lstrip(' ')
                        enteredY = enteredY.rstrip(' ')
                        if enteredX[0] == '-':
                            x, y = int(enteredX), int(enteredY)
                            raise IndexError
                        elif enteredY[0] == '-':
                            x, y = int(enteredX), int(enteredY)
                            raise IndexError
                        if not enteredX.isnumeric():
                            print(f"Row should be an integer. {enteredX} is NOT an integer.")
                            x, y = None, None
                            continue
                        elif not enteredY.isnumeric():
                            print(f"Column should be an integer. {enteredY} is NOT an integer.")
                            x, y = None, None
                            continue
                        x, y = int(enteredX), int(enteredY)
                        continue
                    if (curPlayer.scanningBoard.contents[x][y] != '*'):
                        print(f"You have already fired at {x}, {y}.")
                        x, y = None, None
                        continue
                    break
                break
            except IndexError: #bound error
                print(f"{x}, {y} is not in bounds of our {self.playerBoard.numRows} X {self.playerBoard.numCols} board.")
                x, y = None, None
                continue
            except ValueError:
                print(f"{entered} is not a valid location.")
                print("Enter the firing location in the form row, column")
                x, y = None, None
                continue
        curPlayer.fire(otherPlayer, x, y)

    def fire(self, otherPlayer : "Player", x : int, y : int):
        if otherPlayer.playerBoard.contents[x][y] == otherPlayer.playerBoard.blankChar:
            self.scanningBoard.contents[x][y] = 'O'
            otherPlayer.playerBoard.contents[x][y] = 'O'
            print(f"Miss")
        else:
            temp = otherPlayer.playerBoard.contents[x][y]
            self.scanningBoard.contents[x][y] = 'X'
            otherPlayer.playerBoard.contents[x][y] = 'X'
            for key, value in otherPlayer.playerBoard.shipsOnBoard.items():
                if key.startswith(temp):
                    otherPlayer.playerBoard.shipsOnBoard[key] -= 1
                    print(f"You hit {otherPlayer.name}'s {key}!")
                    if otherPlayer.playerBoard.shipsOnBoard[key] == 0:
                        print(f"You destroyed {otherPlayer.name}'s {key}")
            self.hitCounter += 1
        pass

    @staticmethod
    def getNameFromPlayer(otherPlayers: Iterable["Player"]) -> str:
        alreadyUsedNames = set([player.name for player in otherPlayers])
        while True: # this loops until a player enters a unique name
            i = len(alreadyUsedNames) + 1
            name = input(f"Player {i} please enter your name: ")
            if name not in alreadyUsedNames:
                return name
            else:
                print(f"Someone is already using {name} for their name.")
                print("Please choose another name.")

    def __str__(self) -> str:
        return self.name

if __name__ == "__main__":
    pass