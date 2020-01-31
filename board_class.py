from typing import Iterable, Set, Tuple, Dict, List, Iterator
import sys
from ship_class import Ship


class Board:
    def __init__(self, numRows: int, numCols: int, blankChar: str) -> None:
        self.contents = []
        self.numCols = numCols
        self.numRows = numRows
        self.blankChar = blankChar
        self.contents = [[blankChar for col in range(numCols)] for row in range(numRows)]

    @property
    def numCols(self):
        return len(self.numCols)

    @property
    def numRows(self):
        return len(self.numRows)

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

    def placeShips(self, ship : Ship):#listOfShips : List[Ship]): # takes player ship object from the list passed to it, and uses the assigned location to place the ship on the playerBoard
        #for ship in range(len(listOfShips)):
        #    if listOfShips[ship].orientation == 'h':
        #        x = listOfShips[ship].locationX
        #        y = listOfShips[ship].locationY
        #        for i in range(listOfShips[ship].shipSize):
        #            self.contents[x][y] = listOfShips[ship].shipLetter
        #            y += 1
        #    elif listOfShips[ship].orientation == 'v':
        #        x = listOfShips[ship].locationX
        #        y = listOfShips[ship].locationY
        #        for j in range(listOfShips[ship].shipSize):
        #            self.contents[x][y] = listOfShips[ship].shipLetter
        #            x += 1
        if ship.orientation == 'h':
            x = ship.locationX
            y = ship.locationY
            for i in range(ship.shipSize):
                self.contents[x][y] = ship.shipLetter
                ship.placementPosY.append(y)
                y += 1
        elif ship.orientation == 'v':
            x = ship.locationX
            y = ship.locationY
            for j in range(ship.shipSize):
                self.contents[x][y] = ship.shipLetter
                ship.placementPosX.append(x)
                x += 1


if __name__ == "__main__":
    pass
