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

    def play(self):
        quitGame = ''
        while quitGame != 'y':
            self.openingMenu()
            self.game()
            quitGame = input("Quit game? [y] or [n]\n")

    def openingMenu(self):
        print("💣Welcome to Minesweeper💣\n")
        difficulty = ''
        while difficulty.lower() != 'e' or 'm' or 'h' or 'c':
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
        pattern = re.compile("(\d+) *, *(\d+)")
        win = False
        while not win:
            for x in range(self.board.numRows - 1):
                for y in range(self.board.numColumns - 1):
                    print(self.board.table[x][y])
                    if y == self.board.numColumns - 1:
                        print("\n")
            prompt = ""
            while prompt.lower() == "normal" or "flag" or pattern.match(prompt):
                prompt = input("Enter coordinates in the form \"x, y\"\nor write selection type (normal or flag): ")

                if prompt.lower() == "normal":
                    self.isFlagSelect = False
                elif prompt.lower() == "flag":
                    self.isFlagSelect = True
            m = pattern.match(prompt)
            if m:
                x = m.groups(1)
                y = m.groups(2)
                if not self.isFlagSelect:
                    self.board.table[x][y].open()
                    if self.board.table[x][y].hasMine:
                        print("Game over!\n")
                        break
                else:
                    self.board.table[x][y].flag()



