from typing import Iterable, Set, Tuple, Dict, List
import sys
from game_class import Game
from player_class import Player
from ship_class import Ship

class Board:
    def __init__(self, numRows: int, numCols: int, blankChar: str) -> None:
        self.contents = []
        for row in range(numRows):
            for col in range(numCols):
                self.contents.append(blankChar)
        self.blank_char = blankChar

    def __str__(self) -> str:
        sep = ' ' * max([len(str(self.numRows)), len(str(self.numCols))])
        rep = sep * 2 + sep.join((str(i) for i in range(self.numCols))) + '\n'
        for i, row in enumerate(self):
            rep += str(i) + sep + sep.join(row) + '\n'
        return rep

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
