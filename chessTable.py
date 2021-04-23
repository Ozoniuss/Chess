from Domain.Pieces.Bishop import Bishop
from Domain.Pieces.BoardPiece import BoardPiece
from Domain.Pieces.EmptyPiece import EmptyPiece
from Domain.Pieces.King import King
from Domain.Pieces.Knight import Knight
from Domain.Pieces.NotOnBoard import NotOnBoard
from Domain.Pieces.Pawn import Pawn
from Domain.Pieces.Queen import Queen
from Domain.Pieces.Rock import Rock
from typing import *

class ChessTable:

    # table is stored as a dict, with the positions being the keys.
    # (1,1) is the bottom left corner (white) and (8,8) is top right (black)
    def __init__(self):
        self.__table = {}
        for x in range(1, 9):
            for y in range(1, 9):
                self.__table[(x, y)] = EmptyPiece()

        # stores the list of moves, convention:
        self.__list_of_moves = []
        self.__white_king_pos = None
        self.__black_king_pos = None

        self.white_king_moved = False
        self.black_king_moved = False

        self.white_rock_left_moved = False
        self.white_rock_right_moved = False
        self.black_rock_left_moved = False
        self.black_rock_right_moved = False

    # returns the chess table
    def get_table(self) -> Dict[Tuple[int, int], BoardPiece]:
        return self.__table

    def get_list_of_moves(self) -> List[Tuple[BoardPiece, Tuple[int, int], Tuple[int, int]]]:
        # the piece, the new square and the original square
        return self.__list_of_moves

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
    def move_piece(self, x, y, new_x, new_y, promotion_piece = EmptyPiece()):
        piece = self.get_piece(x, y)
        if piece.get_piece_color_and_type()[0] == 'white' or piece.get_piece_color_and_type()[0] == 'black':

            # needs to be a valid move
            if (new_x, new_y) not in self.get_piece(x, y).get_available_moves(self, x, y):
                raise Exception("Invalid move!")

            # make the move, also eliminates opponent piece if needed
            old_piece = self.__table[(new_x, new_y)] # will be used for en passant
            self.__table[(new_x, new_y)] = self.__table[(x, y)]
            self.__table[(x, y)] = EmptyPiece()

            # these are all for castling
            if x == 1 and y == 1 and piece.get_piece_color_and_type() == ('white', 'rock'):
                self.white_rock_left_moved = True
            if x == 8 and y == 1 and piece.get_piece_color_and_type() == ('white', 'rock'):
                self.white_rock_right_moved = True
            if x == 1 and y == 8 and piece.get_piece_color_and_type() == ('black', 'rock'):
                self.black_rock_left_moved = True
            if x == 8 and y == 8 and piece.get_piece_color_and_type() == ('black', 'rock'):
                self.black_rock_right_moved = True

            if x == 5 and y == 1 and piece.get_piece_color_and_type() == ('white', 'king'):
                self.white_king_moved = True
            if x == 5 and y == 8 and piece.get_piece_color_and_type() == ('black', 'king'):
                self.black_king_moved = True


            # en passant
            # basically, the only possible time a pawn moves diagonally on a square that had an empty piece is en passant
            if piece.get_piece_color_and_type()[1] == 'pawn' and abs(new_x - x) + abs(new_y - y) == 2 and \
                    old_piece.get_piece_color_and_type() == (None, None):
                self.__table[(new_x, y)] = EmptyPiece()

            # white left castles, all is left is to move the rock
            if piece.get_piece_color_and_type() == ('white','king') and new_x - x == -2:
                self.__table[(x-4,y)] = EmptyPiece()
                self.__table[(new_x+1, y)] = Rock('white')

            # white right castles
            if piece.get_piece_color_and_type() == ('white','king') and new_x - x == 2:
                self.__table[(x+3,y)] = EmptyPiece()
                self.__table[(new_x-1, y)] = Rock('white')

            # black left castles
            if piece.get_piece_color_and_type() == ('black','king') and new_x - x == -2:
                self.__table[(x-4,y)] = EmptyPiece()
                self.__table[(new_x+1, y)] = Rock('black')

            # black right castles
            if piece.get_piece_color_and_type() == ('black','king') and new_x - x == 2:
                self.__table[(x+3,y)] = EmptyPiece()
                self.__table[(new_x-1, y)] = Rock('black')


            # pawn reaches the end and can promote
            if piece.get_piece_color_and_type() == ('white', 'pawn') and y == 7 and new_y == 8:
                self.__table[(new_x, new_y)] = promotion_piece

            # same for black pawn
            if piece.get_piece_color_and_type() == ('black', 'pawn') and y == 2 and new_y == 1:
                self.__table[(new_x, new_y)] = promotion_piece


            # add the move to the list of moves
            self.__list_of_moves.append((piece, (new_x, new_y), (x, y)))


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

# table = ChessTable()
# table.populate_chess_table()
# print(len(table.get_table().keys()))
# print(table)

