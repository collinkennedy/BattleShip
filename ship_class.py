from typing import Iterable, Set, Tuple, Dict, List
import sys
#from game_class import Game
#from player_class import Player
#from board_class import Board


class Ship:
    def __init__(self, index: int):
        self.name = self.getShipName(listOfShips)
        self.size = self.getShipSize(listOfShips)
        self.location : List[int] = None
        self.orientation : str = None # h or v

    @staticmethod
    def getShipName() -> str:
        return self.name

    @staticmethod
    def readFileShips() -> Iterable[Dict]:
        dictOfShips = {}
        with open(sys.argv[1]) as file:
            for i, line in enumerate(file):
                if i == 0:
                    continue
                else:
                    shipName, shipSize = line.split(" ")
                    if len(shipSize) > 1:
                        shipSize = shipSize[:-1]
                    dictOfShips[shipName] = shipSize
        return dictOfShips


if __name__ == "__main__":
    print(Ship.readFileShips())
