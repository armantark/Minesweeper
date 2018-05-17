from Board import Board
import re

EASYROWS = 9
EASYCOLS = 9
EASYMINES = 10
MEDROWS = 16
MEDCOLS = 16
MEDMINES = 40
HARDROWS = 16
HARDCOLS = 30
HARDMINES = 99


class Game:
    board = None
    isFlagSelect = False

    def __init__(self):
        pass

    def play(self):
        quitGame = ''
        while quitGame != 'y':
            self.openingMenu()
            self.game()
            quitGame = input("Quit game? [y] or [n]\n")

    def openingMenu(self):
        print("💣Welcome to Minesweeper💣\n")
        difficulty = ''
        while difficulty.lower() != 'e' \
                and difficulty.lower() != 'm' \
                and difficulty.lower() != 'h' \
                and difficulty.lower() != 'c':
            difficulty = input("[E]asy, [m]edium, [h]ard, or [c]ustom?\n")
        if difficulty.lower() == 'e':
            self.board = Board(EASYROWS, EASYCOLS, EASYMINES)
        elif difficulty.lower() == 'm':
            self.board = Board(MEDROWS, MEDCOLS, MEDMINES)
        elif difficulty.lower() == 'h':
            self.board = Board(HARDROWS, HARDCOLS, HARDMINES)
        else:
            customrows, customcols, custommines = '', '', ''
            while not customrows.isnumeric():
                customrows = input("Number rows: ")
            while not customcols.isnumeric():
                customcols = input("Number columns: ")
            while not custommines.isnumeric() and custommines > int(customcols) * int(customrows):
                custommines = input("Number mines (cannot be more than rows * cols): ")
            self.board = Board(int(customrows), int(customcols), int(custommines))

    def game(self):
        pattern = re.compile("(\d+) *, *(\d+)")  # regex for coords
        while True:
            self.printBoard()
            if not self.isFlagSelect:
                print("Current selection type: Normal")
            else:
                print("Current selection type: Flag")
            if self.board.numCurrOpened == self.board.numRows * self.board.numColumns - self.board.numMines:
                print("YOU WIN!")
                break
            prompt = ""
            while prompt.lower() == "normal" or prompt.lower() == "flag" or not pattern.match(prompt):
                prompt = input("Enter coordinates in the form \"x, y\"\nor write selection type ([n]ormal or [f]lag): ")
                if prompt.lower() == "normal" or prompt.lower() == "n":
                    self.isFlagSelect = False
                elif prompt.lower() == "flag" or prompt.lower() == "f":
                    self.isFlagSelect = True
            m = pattern.match(prompt)
            if m:
                x = int(m.groups()[0]) - 1
                y = int(m.groups()[1]) - 1
                if not self.isFlagSelect:
                    try:
                        self.board.table[x][y].open()
                        if self.board.table[x][y].hasMine:
                            self.printBoard()
                            print("Game over!\n")
                            break
                    except IndexError:
                        print("Bad coords!")
                else:
                    self.board.table[x][y].flag()

    # this should be __str__ of board, will move later
    def printBoard(self):
        print("  ", end='')
        for i in range(self.board.numColumns):
            print(i + 1, end='')
            print(" ", end='')
        print("\n\n", end='')
        print("1 ", end='')
        for x in range(self.board.numRows):
            for y in range(self.board.numColumns):
                print(self.board.table[x][y], end='')
                if y == self.board.numColumns - 1:
                    print("\n", end='')
                    if (x != self.board.numRows - 1):
                        print(x + 2, end='')
                        print(" ", end='')
