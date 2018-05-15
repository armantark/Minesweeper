from Cell import Cell


class Board:
    table = [[]]
    numRows = 0
    numColumns = 0

    def __init__(self, numRows, numColumns):
        self.numRows = numRows
        self.numColumns = numColumns
        self.randomizeBoard()

    def randomizeBoard(self):
        for x in range(self.numRows):
            for y in range(self.numColumns):
                self.table[x][y] = Cell((x, y), self)

