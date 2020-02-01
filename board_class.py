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
        self.lettersOnBoard = []
        self.contents = [[blankChar for col in range(numCols)] for row in range(numRows)]

    @property
    def numCols(self):
        return len(self.numCols)

    @property
    def numRows(self):
        return len(self.numRows)

    def getListOfShips(self):
        returnedDictOfShips = Ship.readFileShips()
        for shipName, shipSize in returnedDictOfShips.items(): # create a ship object with those attributes and store it in a list
            newShip = Ship(shipName, shipSize)
            self.listOfPlayerShips.append(newShip)
        print(self.listOfPlayerShips)
        return self.listOfPlayerShips

    def __str__(self) -> str:
        sep = ' ' * max([len(str(self.numRows)), len(str(self.numCols))])
        rep = sep * 2 + sep.join((str(i) for i in range(self.numCols))) + '\n'
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)

    def __getitem__(self, i: int) -> List[str]:
        self.contents[i]

    # @property
    def numCols(self):
        return len(self.numCols)

    # @property
    def numRows(self):
        return len(self.numRows)

    def boundCheck(self, ship: "Ship", row: int, col: int):
        # call this method each time user places a ship
        # checks if the entirety of the ship being placed
        # will fit in bounds
        pass

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


    #def placeShips(self, ship: "Ship", tempX: int, tempY: int, tempOrientation: str):
    #    if self.takenCoords != []:
    #        testingCoords = True
    #        testableCoords = []
    #        for i in range(ship.shipSize):
    #            testableCoords.append(tuple(tempX, tempY))
    #            if ship.orientation == 'h':
    #                tempY += 1
    #            elif ship.orientation == 'v':
    #                tempX += 1
    #        print(testableCoords)
    #        while testingCoords:
    #            for testableCoordsTuple in testableCoords:
    #                for i in self.takenCoords:
    #                    if testableCoordsTuple == self.takenCoords[i]:
    #                        tempX, tempY = input("Please enter a non-overlapping position: ").split(",")
    #                        testableCoords = []
    #                        for i in range(ship.shipSize):
    #                            testableCoords.append(tuple(tempX, tempY))
    #                            if ship.orientation == 'h':
    #                                tempY += 1
    #                            elif ship.orientation == 'v':
    #                                tempX += 1
    #                    else:
    #                        testingCoords = False
    #    else:  # possibly not going into here
    #        if ship.orientation == 'h':
    #            x = tempX
    #            y = tempY
    #            for i in range(ship.shipSize):
    #                self.contents[x][y] = ship.shipLetter
    #                ship.placementPosX.append(x)
    #                ship.placementPosY.append(y)
    #                y += 1
    #        elif ship.orientation == 'v':
    #            x = tempX
    #            y = tempY
    #            for j in range(ship.shipSize):
    #                self.contents[x][y] = ship.shipLetter
    #                ship.placementPosX.append(x)
    #                ship.placementPosY.append(y)
    #                x += 1
    #        zipper = zip(ship.placementPosX, ship.placementPosY)
    #        for posX, posY in zipper:
    #            self.takenCoords.append((posX, posY))
    #        print(self.takenCoords)