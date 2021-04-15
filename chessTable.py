from boardPiece import *


class ChessTable:

    # table is stored as a dict, with the positions being the keys.
    # (1,1) is the bottom left corner (white) and (8,8) is top right (black)
    def __init__(self):
        self.__table = {}
        for x in range(1, 9):
            for y in range(1, 9):
                self.__table[(x, y)] = BoardPiece()

        # stores the list of moves, convention:
        self.__list_of_moves = []
        self.__white_king_pos = None
        self.__black_king_pos = None

    # returns the chess table
    def get_table(self) -> dict:
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

    # return the piece at position (x,y)
    # return a NotOnBoard (subclass of BoardPiece) object if the piece is not on the board
    def get_piece(self, x, y) -> BoardPiece:
        if (x not in range(1, 9)) or (y not in range(1, 9)):
            return NotOnBoard()
        return self.__table[(x, y)]

    # move a piece at position new_x, new_y
    def move_piece(self, x, y, new_x, new_y):
        if self.get_piece(x, y).get_piece_color_and_type()[0] == 'white' or self.get_piece(x, y).get_piece_color_and_type()[0] == 'black':

            # needs to be a valid move
            if (new_x, new_y) not in self.get_piece(x, y).get_available_moves(self, x, y):
                raise Exception("Invalid move!")

            # make the move, also eliminates opponent piece if needed
            self.__table[(new_x, new_y)] = self.__table[(x, y)]
            self.__table[(x, y)] = BoardPiece()



    def populate_chess_table(self):
        self.__white_king_pos = (5, 1)
        self.__black_king_pos = (5, 8)
        # pawns
        for x in range(1, 9):
            self.__table[(x, 7)] = Pawn('black')

        for x in range(1, 9):
            self.__table[(x, 2)] = Pawn('white')

        # other pieces
        self.__table[(1, 1)] = Rock('white')
        self.__table[(8, 1)] = Rock('white')
        self.__table[(1, 8)] = Rock('black')
        self.__table[(8, 8)] = Rock('black')
        self.__table[(2, 1)] = Knight('white')
        self.__table[(7, 1)] = Knight('white')
        self.__table[(2, 8)] = Knight('black')
        self.__table[(7, 8)] = Knight('black')
        self.__table[(3, 1)] = Bishop('white')
        self.__table[(6, 1)] = Bishop('white')
        self.__table[(3, 8)] = Bishop('black')
        self.__table[(6, 8)] = Bishop('black')
        self.__table[(4, 1)] = Queen('white')
        self.__table[(5, 1)] = King('white')
        self.__table[(4, 8)] = Queen('black')
        self.__table[(5, 8)] = King('black')

    def play_game(self):
        pass

table = ChessTable()
table.populate_chess_table()
print(len(table.get_table().keys()))
print(table)

d = {1: '2'}
d[1] = '3'
d[3] = '4'
print(d.get(2))