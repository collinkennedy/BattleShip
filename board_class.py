from typing import Iterable, Set, Tuple, Dict, List, Iterator
import sys
from ship_class import Ship

class Board:
    def __init__(self, numRows: int, numCols: int, blankChar: str) -> None:
        self.contents = []
        self.numCols = numCols
        self.numRows = numRows
        self.blankChar = blankChar
        self.takenCoords = []
        self.shipsOnBoard = {}
        self.UNCHANGEDSHIPSONBOARD = {}
        self.contents = [[blankChar for col in range(numCols)] for row in range(numRows)]

    def getListOfShips(self):
        returnedDictOfShips = Ship.readFileShips()
        for shipName, shipSize in returnedDictOfShips.items(): # create a ship object with those attributes and store it in a list
            newShip = Ship(shipName, shipSize)
            self.listOfPlayerShips.append(newShip)
        print(self.listOfPlayerShips)
        return self.listOfPlayerShips

    def __str__(self) -> str:
        space = ' ' * max([len(str(self.numRows)), len(str(self.numCols))])
        repeat = space * 2 + space.join((str(i) for i in range(self.numCols))) + '\n'
        for rowIndex, row in enumerate(self):
            repeat += str(rowIndex) + space + space.join(row) + '\n'
        return repeat

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)

    def __getitem__(self, i: int) -> List[str]:
        self.contents[i]

    def numCols(self):
        return len(self.numCols)

    def numRows(self):
        return len(self.numRows)

    def badValues(self, ship: Ship, x, y, board: "Board", maxX, maxY, player) -> bool:
        if ship.orientation == 'h':  # y varies here, x does not need to change
            for i in range(ship.shipSize):
                if board.contents[x][y] != self.blankChar:  # if the location provided is occupied, return true
                    myTestY = y
                    for i in range(ship.shipSize):
                        if (self.contents[x][myTestY] != self.blankChar):
                            player.overlappingShips.append(board.contents[x][myTestY])
                            myTestY += 1
                    player.overlappingShips.sort()
                    return True  # your values suck
                y += 1
            return False  # good job
        elif ship.orientation == 'v':  # x varies here
            for i in range(ship.shipSize):
                if self.contents[x][y] != self.blankChar:  # if the location provided is occupied, return true
                    myTestX = x
                    for i in range(ship.shipSize):
                        if (self.contents[myTestX][y] != self.blankChar):
                            player.overlappingShips.append(board.contents[myTestX][y])
                            myTestX += 1
                    player.overlappingShips.sort()
                    return True  # your values suck
                x += 1
            return False  # good job

    def placeShip(self, ship: Ship, x: int, y: int, board: "Board"):
        if ship.orientation == 'h':
            for i in range(ship.shipSize):
                board.contents[x][y] = ship.shipLetter
                y += 1
        elif ship.orientation == 'v':
            for i in range(ship.shipSize):
                board.contents[x][y] = ship.shipLetter
                x += 1

if __name__ == "__main__":
    pass