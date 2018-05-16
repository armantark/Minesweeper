from random import random

from Cell import Cell


class Board:
    table = [[Cell]]
    numRows = 0
    numColumns = 0
    numMines = 0

    def __init__(self, numRows: int, numColumns: int, numMines: int):
        self.numRows = numRows
        self.numColumns = numColumns
        self.numMines = numMines
        self.randomizeBoard()

    def randomizeBoard(self):
        currNumMines = 0
        for x in range(self.numRows):
            for y in range(self.numColumns):
                hasMine = False
                if currNumMines < self.numMines:
                    hasMine = random() < self.numMines/(self.numRows*self.numColumns)
                    currNumMines += 1
                self.table[x][y] = Cell((x, y), self, hasMine)
        for x in range(self.numRows):
            for y in range(self.numColumns):
                self.table[x][y].calculateNumberOfMines()

