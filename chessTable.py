from boardPiece import *


class ChessTable:
    def __init__(self):
        self.__table = {}
        for x in range(1, 9):
            for y in range(1, 9):
                self.__table[(x, y)] = BoardPiece()

        # stores the list of moves, convention:
        self.__list_of_moves = []

    def get_table(self):
        return self.__table

    def __str__(self):
        out = ''
        for y in range(8, 0, -1):
            out += str(y) + ' '
            for x in range(1, 9):
                out += str(self.__table[(x, y)]) + ' '
            out += '\n'
        out += '  A B C D E F G H'
        return out

    # return a piece at a certain position
    def get_piece(self, x, y):
        if (x not in range(1, 9)) or (y not in range(1, 9)):
            return NotOnBoard()
        return self.__table[(x, y)]

    def populate_chess_table(self):

        # pawns
        for x in range(1, 9):
            self.__table[(x, 7)] = Pawn('red')

        # for x in range(1, 9):
        #     self.__table[(x, 2)] = Pawn('blue')

        # other pieces
        self.__table[(1, 1)] = Rock('blue')
        self.__table[(8, 1)] = Rock('blue')
        self.__table[(1, 8)] = Rock('red')
        self.__table[(8, 8)] = Rock('red')
        self.__table[(2, 1)] = Knight('blue')
        self.__table[(7, 1)] = Knight('blue')
        self.__table[(2, 8)] = Knight('red')
        self.__table[(7, 8)] = Knight('red')
        self.__table[(3, 1)] = Bishop('blue')
        self.__table[(6, 1)] = Bishop('blue')
        self.__table[(3, 8)] = Bishop('red')
        self.__table[(6, 8)] = Bishop('red')
        self.__table[(4, 1)] = Queen('blue')
        self.__table[(5, 1)] = King('blue')
        self.__table[(4, 8)] = Queen('red')
        self.__table[(5, 8)] = King('red')

    def play_game(self):
        pass

table = ChessTable()
table.populate_chess_table()
print(table)
