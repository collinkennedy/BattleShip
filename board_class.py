class Board:
    
    def __init__(self, numRows: int, numCols: int, blankChar: str) -> None:
        self.contents = []
        for row in range(numRows):
            for col in range(numCols):
                self.contents.append(blankChar)
        self.blank_char = blankChar

    def __str__(self) -> str:
        sep = ' ' * max([len(str(self.num_rows)), len(str(self.num_cols))])
        rep = sep * 2 + sep.join((str(i) for i in range(self.num_cols))) + '\n'
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

if __name__== "__main__":
    pass