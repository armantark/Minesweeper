from random import randint

from Cell import Cell


class Board:
    table = None
    numRows = 0
    numColumns = 0
    numMines = 0
    numCurrOpened = 0

    def __init__(self, numRows: int, numColumns: int, numMines: int):
        self.numRows = numRows
        self.numColumns = numColumns
        self.numMines = numMines
        self.table = [[Cell() for _ in range(numRows)] for _ in range(numColumns)]
        self.randomizeBoard()

    def randomizeBoard(self):
        randomindices = set([])
        while len(randomindices) != self.numMines:
            randomindices.add((randint(0, self.numRows - 1), randint(0, self.numColumns - 1)))
        for y in range(self.numRows):
            for x in range(self.numColumns):
                hasMine = False
                if (x, y) in randomindices:
                    hasMine = True
                self.table[x][y] = Cell((x, y), self, hasMine)
        for y in range(self.numRows):
            for x in range(self.numColumns):
                self.table[x][y].calculateNumberOfMines()

