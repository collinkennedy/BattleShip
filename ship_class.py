from typing import Iterable, Set, Tuple
import sys

class Ship:
    def __init__(self, index :int):
        self.name = self.getShipName(listOfShips)
        self.size = self.getShipSize(listOfShips)

    @staticmethod
    def getShipName() -> str:
        pass

    @staticmethod
    def readFileShips() -> Iterable[Dict]:
        dictOfShips = {}
        with open(sys.argv[1]) as file:
            for i, line in enumerate(file):
                if i == 0:
                    continue
                else:
                    shipName, shipSize = line.split(" ")
                    dictOfShips[shipSize] = shipName
        return dictOfShips




if __name__ == "__main__":
    pass