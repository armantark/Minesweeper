from random import randint

from Cell import Cell

from colorama import Fore, Back, Style

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
            randomindices.add((randint(0, self.numColumns - 1), randint(0, self.numRows - 1)))
        for y in range(self.numRows):
            for x in range(self.numColumns):
                hasMine = False
                if (x, y) in randomindices:
                    hasMine = True
                self.table[x][y] = Cell((x, y), self, hasMine)
        for y in range(self.numRows):
            for x in range(self.numColumns):
                self.table[x][y].calculateNumberOfMines()

    # this is f**ky, fix later
    def __str__(self):
        print("  ", end='')
        if len(str(self.numRows)) == 2:
            print(" ", end='')
        for i in range(self.numColumns):
            if len(str(i + 1)) == 2:
                print(Back.RED + Fore.YELLOW, end='')
                print(str(i + 1)[0], end='')
                print(Style.RESET_ALL, end='')
            else:
                print(Back.RED + Fore.YELLOW, end='')
                print(i + 1, end='')
                print(Style.RESET_ALL, end='')
            print(" ", end='')

        if len(str(self.numColumns)) == 2:
            print('')
            print("  ", end='')
            if len(str(self.numRows)) == 2:
                print(" ", end='')
            for i in range(self.numColumns):
                if len(str(i + 1)) == 2:
                    print(Back.RED + Fore.YELLOW, end='')
                    print(str(i + 1)[1], end='')
                    print(Style.RESET_ALL, end='')
                else:
                    print(" ", end='')
                print(" ", end='')
        print("\n")
        if len(str(self.numRows)) == 2:
            print(" ", end='')
        print(Back.RED + Fore.YELLOW, end='')
        print("1", end='')
        print(Style.RESET_ALL + " ", end='')
        for y in range(self.numRows):
            for x in range(self.numColumns):
                print(self.table[x][y], end='')
                if x == self.numColumns - 1:
                    print("\n", end='')
                    if y != self.numRows - 1:
                        if len(str(self.numRows)) == 2 and len(str(y + 2)) != 2:
                            print(" ", end='')
                        print(Back.RED + Fore.YELLOW, end='')
                        print(y + 2, end='')
                        print(Style.RESET_ALL, end='')
                        print(" ", end='')
