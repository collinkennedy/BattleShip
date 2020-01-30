from typing import Iterable


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

    def __iter__(str) -> Iterable[List[str]]:
        return iter(self.contents)

    @property
    def numCols(self):
        return len(self.numCols)

    @property
    def numRows(self):
        return len(self.numRows)



if __name__== "__main__":
    pass