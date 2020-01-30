from typing import Iterable, Set, Tuple, Dict, List, Iterator
import sys
#from game_class import Game
from player_class import Player
from ship_class import Ship

class Board:
    def __init__(self, numRows: int, numCols: int, blankChar: str) -> None:
        self.contents = []
        for row in range(numRows):
            for col in range(numCols):
                self.contents.append(blankChar)
        self.blankChar = blankChar

    def __str__(self) -> str:
        sep = ' ' * 1
        rep = sep * 2 + sep.join((str(i) for i in range(2))) + '\n'
        for i, row in enumerate(self):
            rep += str(i) + sep + sep.join(row) + '\n'
        return rep
        #sep = ' ' * max([len(str(self.numRows)), len(str(self.numCols))])
        #rep = sep * 2 + sep.join((str(i) for i in range(self.numCols))) + '\n'
        #for row_index, row in enumerate(self):
        #    rep += str(row_index) + sep + sep.join(row) + '\n'
        #return rep
        #for i in range(7):
        #    for j in range(1):
        #        print('* ' * 7)



    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)

    def __getitem__(self, i: int) -> List[str]:
        self.contents[i]

    @property
    def numCols(self):
        return len(self.numCols)

    @property
    def numRows(self):
        return len(self.numRows)

    def boundCheck(self, ship: "Ship", row: int, col: int):
        # call this method each time user places a ship
        # checks if the entirety of the ship being placed
        # will fit in bounds
        pass


if __name__ == "__main__":
    pass
