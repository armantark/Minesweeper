import Board


class Cell:
    board = None
    coordinate = (-1, -1)
    isOpened = False
    hasFlag = False
    hasMine = False
    numberOfMines = 0

    def __init__(self):
        pass

    def __init__(self, coords: tuple = (-1, -1), board: Board = None, hasMine: bool = False):
        self.coordinate = (coords[0], coords[1])
        self.board = board
        self.hasMine = hasMine

    def calculateNumberOfMines(self):
        x = self.coordinate[0]
        y = self.coordinate[1]
        try:
            if y - 1 >= 0:
                if x - 1 >= 0:
                    if self.board.table[x - 1][y - 1].hasMine:  # nw
                        self.numberOfMines += 1
                if self.board.table[x + 0][y - 1].hasMine:  # w
                    self.numberOfMines += 1
                try:
                    if self.board.table[x + 1][y - 1].hasMine:  # sw
                        self.numberOfMines += 1
                except IndexError:
                    pass
            if x - 1 >= 0:
                if self.board.table[x - 1][y + 0].hasMine:  # n
                    self.numberOfMines += 1
                try:
                    if self.board.table[x - 1][y + 1].hasMine:  # nw
                        self.numberOfMines += 1
                except IndexError:
                    pass
            try:
                if self.board.table[x + 1][y + 0].hasMine:  # s
                    self.numberOfMines += 1
            except IndexError:
                pass
            try:
                if self.board.table[x + 0][y + 1].hasMine:  # e
                    self.numberOfMines += 1
            except IndexError:
                pass
            try:
                if self.board.table[x + 1][y + 1].hasMine:  # se
                    self.numberOfMines += 1
            except IndexError:
                pass
        except IndexError:
            pass
        except AttributeError:
            pass

    def open(self):
        if self.hasMine:
            self.isOpened = True
        if not self.isOpened and not self.hasMine:
            self.isOpened = True
            x = self.coordinate[0]
            y = self.coordinate[1]
            if self.numberOfMines == 0:
                try:
                    if y - 1 >= 0:
                        if x - 1 >= 0:
                            Cell.open(self.board.table[x - 1][y - 1])  # nw
                        Cell.open(self.board.table[x - 0][y - 1])  # w
                        try:
                            Cell.open(self.board.table[x + 1][y - 1])  # sw
                        except IndexError:
                            pass
                    if x - 1 >= 0:
                        Cell.open(self.board.table[x - 1][y - 0])  # n
                        try:
                            Cell.open(self.board.table[x - 1][y + 1])  # ne
                        except IndexError:
                            pass
                    try:
                        Cell.open(self.board.table[x + 1][y + 1])  # se
                    except IndexError:
                        pass
                    try:
                        Cell.open(self.board.table[x + 1][y - 0])  # s
                    except IndexError:
                        pass
                    try:
                        Cell.open(self.board.table[x - 0][y + 1])  # e
                    except IndexError:
                        pass
                except IndexError:
                    pass
            self.board.numCurrOpened += 1

    def flag(self):
        self.hasFlag = not self.hasFlag

    def __str__(self):
        if self.hasFlag:
            return "⚑ "
        elif not self.isOpened:
            return "= "
        else:
            if self.hasMine:
                return "* "
            else:
                return str(self.numberOfMines) + " "
