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
            while not customrows.isnumeric() or len(customrows) > 2:
                customrows = input("Number rows (can only be 2 digit number): ")
            while not customcols.isnumeric() or len(customcols) > 2:
                customcols = input("Number columns (can only be 2 digit number): ")
            while not custommines.isnumeric() or int(custommines) > int(customcols) * int(customrows) - 1:
                custommines = input("Number mines (cannot be more than rows * cols): ")
            self.board = Board(int(customrows), int(customcols), int(custommines))

    def game(self):
        pattern = re.compile("(\d+) *, *(\d+)")  # regex for coords
        while True:
            try:
                print(self.board)
            except TypeError:
                pass
            if self.board.numCurrOpened == self.board.numRows * self.board.numColumns - self.board.numMines:
                print("YOU WIN!")
                break
            prompt = ""
            while prompt.lower() == "normal" or prompt.lower() == "flag" or not pattern.match(prompt):
                if not self.isFlagSelect:
                    print("Current selection type: Normal")
                else:
                    print("Current selection type: Flag")
                prompt = input("Enter coordinates in the form \"x, y\"\nor write selection type ([n]ormal or [f]lag): ")
                if prompt.lower() == "normal" or prompt.lower() == "n":
                    self.isFlagSelect = False
                elif prompt.lower() == "flag" or prompt.lower() == "f":
                    self.isFlagSelect = True
            m = pattern.match(prompt)
            if m:
                y = int(m.groups()[0]) - 1
                x = int(m.groups()[1]) - 1
                if not self.isFlagSelect:
                    try:
                        self.board.table[x][y].open()
                        if self.board.table[x][y].hasMine:
                            for y in range(self.board.numRows):
                                for x in range(self.board.numColumns):
                                    if self.board.table[x][y].hasMine:
                                        self.board.table[x][y].open()
                            try:
                                print(self.board)
                            except TypeError:
                                pass
                            print("Game over!")
                            break
                    except IndexError:
                        print("Bad coords!")
                else:
                    self.board.table[x][y].flag()
