from Board import Board


class Cell:
    board = None
    coordinate = (-1, -1)
    isOpened = False
    hasFlag = False
    hasMine = False
    numberOfMines = 0

    def __init__(self, coords: tuple, board: Board, hasMine: bool):
        self.coordinate = (coords[0], coords[1])
        self.board = board
        self.hasMine = hasMine

    def calculateNumberOfMines(self):
        try:
            if self.board.table[self.coordinate[0] - 1][self.coordinate[0] - 1].hasMine: #nw
                self.numberOfMines += 1
            if self.board.table[self.coordinate[0] - 1][self.coordinate[0] + 0].hasMine: #n
                self.numberOfMines += 1
            if self.board.table[self.coordinate[0] - 1][self.coordinate[0] + 1].hasMine: #ne
                self.numberOfMines += 1
            if self.board.table[self.coordinate[0] + 0][self.coordinate[0] - 1].hasMine: #w
                self.numberOfMines += 1
            if self.board.table[self.coordinate[0] + 0][self.coordinate[0] + 1].hasMine: #e
                self.numberOfMines += 1
            if self.board.table[self.coordinate[0] + 1][self.coordinate[0] - 1].hasMine: #sw
                self.numberOfMines += 1
            if self.board.table[self.coordinate[0] + 1][self.coordinate[0] + 0].hasMine: #s
                self.numberOfMines += 1
            if self.board.table[self.coordinate[0] + 1][self.coordinate[0] + 1].hasMine: #se
                self.numberOfMines += 1
        except IndexError:
            pass

    def open(self):
        self.isOpened = True

    def flag(self):
        self.hasFlag = True

    def __str__(self):
        if self.hasFlag:
            return "⚑"
        elif not self.isOpened:
            return "⃞"
        else:
            if self.hasMine:
                return "💣"
            else:
                return self.numberOfMines

