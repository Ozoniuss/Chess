from Domain.Pieces.BoardPiece import *
from Domain.Pieces.EmptyPiece import EmptyPiece
from typing import *
from Domain.Pieces.Rock import Rock
from Domain.PieceTypes.PieceType import PieceType
from Domain.PieceColors.PieceColor import PieceColor

class King(BoardPiece):
    def __init__(self, color: PieceColor):
        super().__init__()
        self.__color = color

    def get_piece_color_and_type(self) -> Tuple[str, PieceType]:
        return self.__color, PieceType.KING

    def get_available_moves(self, board, x, y):

        print(self.is_check(board,x,y))

        # the board is passed as a parameter
        # x, y represent the coordinates of the piece
        # will NOT include positions where the king is in check
        available_moves = []

        # for the moment we remove the king to avoid glitches, like the old position of the king
        #                                                       being in the path of an attack
        board.get_table()[(x, y)] = EmptyPiece()


        # now, we also need to place the king in the actual position that it goes
        # if the king takes a piece, and then is attacked, we don't want to have the other color
        # piece still there to block the attack
        # we'll clear these positions after the computations are made.

        if self.__color == PieceColor.WHITE:
             # UP
            if (board.get_piece(x, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x, y + 1).get_piece_color_and_type()[0] is None):

                # move the king
                previous_piece = board.get_piece(x, y + 1)
                board.get_table()[(x, y + 1)] = King(PieceColor.WHITE)

                if not self.is_check(board, x, y + 1):
                    available_moves.append((x, y + 1))

                # place the piece back
                board.get_table()[(x, y + 1)] = previous_piece


            # DOWN
            if (board.get_piece(x, y - 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x, y - 1).get_piece_color_and_type()[0] is None):

                # move the king
                previous_piece = board.get_piece(x, y - 1)
                board.get_table()[(x, y - 1)] = King(PieceColor.WHITE)

                if not self.is_check(board, x, y - 1):
                    available_moves.append((x, y - 1))

                # place the piece back
                board.get_table()[(x, y - 1)] = previous_piece

            # LEFT
            if (board.get_piece(x - 1, y).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 1, y).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x - 1, y)
                board.get_table()[(x - 1, y)] = King(PieceColor.WHITE)

                if not self.is_check(board, x - 1, y):
                    available_moves.append((x - 1, y))

                board.get_table()[(x - 1, y)] = previous_piece


            # RIGHT
            if (board.get_piece(x + 1, y).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 1, y).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x + 1, y)
                board.get_table()[(x + 1, y)] = King(PieceColor.WHITE)

                if not self.is_check(board, x + 1, y):
                    available_moves.append((x + 1, y))

                board.get_table()[(x + 1, y)] = previous_piece


            # UP RIGHT
            if (board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x + 1, y + 1)
                board.get_table()[(x + 1, y + 1)] = King(PieceColor.WHITE)

                if not self.is_check(board, x + 1, y + 1):
                    available_moves.append((x + 1, y + 1))

                board.get_table()[(x + 1, y + 1)] = previous_piece


            # DOWN RIGHT
            if (board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x + 1, y - 1)
                board.get_table()[(x + 1, y - 1)] = King(PieceColor.WHITE)

                if not self.is_check(board, x + 1, y - 1):
                    available_moves.append((x + 1, y - 1))

                board.get_table()[(x + 1, y - 1)] = previous_piece


            # UP LEFT
            if (board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x - 1, y + 1)
                board.get_table()[(x - 1, y + 1)] = King(PieceColor.WHITE)

                if not self.is_check(board, x - 1, y + 1):
                    available_moves.append((x - 1, y + 1))

                board.get_table()[(x - 1, y + 1)] = previous_piece


            # DOWN LEFT
            if (board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x - 1, y - 1)
                board.get_table()[(x - 1, y - 1)] = King(PieceColor.WHITE)

                if not self.is_check(board, x - 1, y - 1):
                    available_moves.append((x - 1, y - 1))

                board.get_table()[(x - 1, y - 1)] = previous_piece

            # now check if it can castle
            # only if the king and rock haven't moved


            # king cannot be in check
            if self.is_check(board,x,y) == False:

                # long castle
                if board.get_piece(x-1, y).get_piece_color_and_type()[1] is None and \
                    board.get_piece(x - 2, y).get_piece_color_and_type()[1] is None and \
                    board.get_piece(x-3, y).get_piece_color_and_type()[1] is None and \
                    board.get_piece(x-4, y).get_piece_color_and_type() == (PieceColor.WHITE, PieceType.ROCK):
                    if board.white_king_moved == board.white_rock_left_moved == False:
                        board.get_table()[(x-2,y)] = King(PieceColor.WHITE)
                        board.get_table()[(x-1,y)] = Rock(PieceColor.WHITE)
                        board.get_table()[(x-4,y)] = EmptyPiece()
                        board.get_table()[(x,y)] = EmptyPiece()

                        if not self.is_check(board, x-2, y):
                            available_moves.append((x-2,y))

                        board.get_table()[(x - 2, y)] = EmptyPiece()
                        board.get_table()[(x - 1, y)] = EmptyPiece()
                        board.get_table()[(x - 4, y)] = Rock(PieceColor.WHITE)
                        board.get_table()[(x, y)] = King(PieceColor.WHITE)

                # short castles
                if board.get_piece(x+1, y).get_piece_color_and_type()[1] is None and \
                    board.get_piece(x+2, y).get_piece_color_and_type()[1] is None and \
                    board.get_piece(x+3, y).get_piece_color_and_type() == (PieceColor.WHITE, PieceType.ROCK):
                    if board.white_king_moved == board.white_rock_right_moved == False:
                        board.get_table()[(x+2,y)] = King(PieceColor.WHITE)
                        board.get_table()[(x+1,y)] = Rock(PieceColor.WHITE)
                        board.get_table()[(x+3,y)] = EmptyPiece()
                        board.get_table()[(x,y)] = EmptyPiece()

                        if not self.is_check(board, x+2, y):
                            available_moves.append((x+2,y))

                        board.get_table()[(x + 2, y)] = EmptyPiece()
                        board.get_table()[(x + 1, y)] = EmptyPiece()
                        board.get_table()[(x + 3, y)] = Rock(PieceColor.WHITE)
                        board.get_table()[(x, y)] = King(PieceColor.WHITE)



            board.get_table()[(x, y)] = King(PieceColor.WHITE)  # place the king back




        if self.__color == PieceColor.BLACK:

            # UP
            if (board.get_piece(x, y + 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x, y + 1).get_piece_color_and_type()[0] is None):

                # move the king
                previous_piece = board.get_piece(x, y + 1)
                board.get_table()[(x, y + 1)] = King(PieceColor.BLACK)

                if not self.is_check(board, x, y + 1):
                    available_moves.append((x, y + 1))

                # place the piece back
                board.get_table()[(x, y + 1)] = previous_piece

            # DOWN
            if (board.get_piece(x, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x, y - 1).get_piece_color_and_type()[0] is None):

                # move the king
                previous_piece = board.get_piece(x, y - 1)
                board.get_table()[(x, y - 1)] = King(PieceColor.BLACK)

                if not self.is_check(board, x, y - 1):
                    available_moves.append((x, y - 1))

                # place the piece back
                board.get_table()[(x, y - 1)] = previous_piece

            # LEFT
            if (board.get_piece(x - 1, y).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 1, y).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x - 1, y)
                board.get_table()[(x - 1, y)] = King(PieceColor.BLACK)

                if not self.is_check(board, x - 1, y):
                    available_moves.append((x - 1, y))

                board.get_table()[(x - 1, y)] = previous_piece

            # RIGHT
            if (board.get_piece(x + 1, y).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 1, y).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x + 1, y)
                board.get_table()[(x + 1, y)] = King(PieceColor.BLACK)

                if not self.is_check(board, x + 1, y):
                    available_moves.append((x + 1, y))

                board.get_table()[(x + 1, y)] = previous_piece


            # UP RIGHT
            if (board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x + 1, y + 1)
                board.get_table()[(x + 1, y + 1)] = King(PieceColor.BLACK)

                if not self.is_check(board, x + 1, y + 1):
                    available_moves.append((x + 1, y + 1))

                board.get_table()[(x + 1, y + 1)] = previous_piece

            # DOWN RIGHT
            if (board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x + 1, y - 1)
                board.get_table()[(x + 1, y - 1)] = King(PieceColor.BLACK)

                if not self.is_check(board, x + 1, y - 1):
                    available_moves.append((x + 1, y - 1))

                board.get_table()[(x + 1, y - 1)] = previous_piece

            # UP LEFT
            if (board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x - 1, y + 1)
                board.get_table()[(x - 1, y + 1)] = King(PieceColor.BLACK)

                if not self.is_check(board, x - 1, y + 1):
                    available_moves.append((x - 1, y + 1))

                board.get_table()[(x - 1, y + 1)] = previous_piece

            # DOWN LEFT
            if (board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] is None):

                previous_piece = board.get_piece(x - 1, y - 1)
                board.get_table()[(x - 1, y - 1)] = King(PieceColor.BLACK)

                if not self.is_check(board, x - 1, y - 1):
                    available_moves.append((x - 1, y - 1))

                board.get_table()[(x - 1, y - 1)] = previous_piece

            # CASTLES

            # king cannot be in check
            if not self.is_check(board, x, y):

                # long castle
                if board.get_piece(x - 1, y).get_piece_color_and_type()[1] is None and \
                        board.get_piece(x - 2, y).get_piece_color_and_type()[1] is None and \
                        board.get_piece(x - 3, y).get_piece_color_and_type()[1] is None and \
                        board.get_piece(x - 4, y).get_piece_color_and_type() == (PieceColor.BLACK, PieceType.ROCK):
                    if board.black_king_moved == board.black_rock_left_moved == False:
                        board.get_table()[(x - 2, y)] = King(PieceColor.BLACK)
                        board.get_table()[(x - 1, y)] = Rock(PieceColor.BLACK)
                        board.get_table()[(x - 4, y)] = EmptyPiece()
                        board.get_table()[(x, y)] = EmptyPiece()

                        if not self.is_check(board, x - 2, y):
                            available_moves.append((x - 2, y))

                        board.get_table()[(x - 2, y)] = EmptyPiece()
                        board.get_table()[(x - 1, y)] = EmptyPiece()
                        board.get_table()[(x - 4, y)] = Rock(PieceColor.BLACK)
                        board.get_table()[(x, y)] = King(PieceColor.BLACK)

                # short castles
                if board.get_piece(x + 1, y).get_piece_color_and_type()[1] is None and \
                        board.get_piece(x + 2, y).get_piece_color_and_type()[1] is None and \
                        board.get_piece(x + 3, y).get_piece_color_and_type() == (PieceColor.BLACK, PieceType.ROCK):
                    if board.black_king_moved == board.black_rock_right_moved == False:
                        board.get_table()[(x + 2, y)] = King(PieceColor.BLACK)
                        board.get_table()[(x + 1, y)] = Rock(PieceColor.BLACK)
                        board.get_table()[(x + 3, y)] = EmptyPiece()
                        board.get_table()[(x, y)] = EmptyPiece()

                        if not self.is_check(board, x + 2, y):
                            available_moves.append((x + 2, y))

                        board.get_table()[(x + 2, y)] = EmptyPiece()
                        board.get_table()[(x + 1, y)] = EmptyPiece()
                        board.get_table()[(x + 3, y)] = Rock(PieceColor.BLACK)
                        board.get_table()[(x, y)] = King(PieceColor.BLACK)

            board.get_table()[(x, y)] = King(PieceColor.BLACK)  # place the king back

        return available_moves

    def get_attacking_spots(self, board, x, y):

        attacking_spots = []

        if self.__color == PieceColor.WHITE:

            if (board.get_piece(x, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x, y + 1))

            if (board.get_piece(x, y - 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x, y - 1))

            if (board.get_piece(x - 1, y).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 1, y).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y))

            if (board.get_piece(x + 1, y).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 1, y).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y))

            if (board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y + 1))

            if (board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y - 1))

            if (board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y + 1))

            if (board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y - 1))

        if self.__color == PieceColor.BLACK:

            if (board.get_piece(x, y + 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x, y + 1))

            if (board.get_piece(x, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x, y - 1))

            if (board.get_piece(x - 1, y).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 1, y).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y))

            if (board.get_piece(x + 1, y).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 1, y).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y))

            if (board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y + 1))

            if (board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y - 1))

            if (board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y + 1))

            if (board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y - 1))

        return attacking_spots

    def __str__(self):
        return 'X'

    def is_check(self, board, x, y):
        # the king is at position x, y. Returns true if the king is in check.

        if self.__color == PieceColor.WHITE:
            for positions in board.get_table():
                # get the color of the piece at each position
                # we are only interested in opposite color pieces:
                piece = board.get_table()[positions]
                if piece.get_piece_color_and_type()[0] == PieceColor.BLACK:
                    # get the positions the piece attacks
                    piece_moves = piece.get_attacking_spots(board, positions[0], positions[1])
                    if (x, y) in piece_moves:
                        return True
            return False

        if self.__color == PieceColor.BLACK:
            for positions in board.get_table():
                # get the color of the piece at each position
                # we are only interested in opposite color pieces:
                piece = board.get_table()[positions]
                if piece.get_piece_color_and_type()[0] == PieceColor.WHITE:
                    # get the positions the piece attacks
                    piece_moves = piece.get_attacking_spots(board, positions[0], positions[1])
                    if (x, y) in piece_moves:
                        return True
            return False