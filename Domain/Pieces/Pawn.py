from Domain.Pieces.BoardPiece import *
from Domain.PieceTypes.PieceType import PieceType
from Domain.PieceColors.PieceColor import PieceColor


class Pawn(BoardPiece):
    # color('red' or 'white') is the color of the pawn
    def __init__(self, color: PieceColor):
        super().__init__()
        self.__color = color

    def get_piece_color_and_type(self):
        return self.__color, PieceType.PAWN

    def get_available_moves(self, board, x: int, y:int):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece
        available_moves = []

        if self.__color == PieceColor.WHITE:
            # right in front
            # if there's a piece ahead there are no moves in front (including beginning)
            # no need to check if valid because we'll never have a pawn on the last row
            #     since it will modify to a different piece

            if board.get_piece(x, y + 1).get_piece_color_and_type()[0] is None:
                available_moves.append((x, y + 1))

                # right at the beginning
                if y == 2 and board.get_piece(x, y + 2).get_piece_color_and_type()[0] is None:
                    available_moves.append((x, y + 2))

            # it can move on the side if there's a white piece
            # no need to check if valid here since it's obviously valid
            if board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK:
                available_moves.append((x - 1, y + 1))
            if board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK:
                available_moves.append((x + 1, y + 1))

            # EN PASSANT ONLY
            if y == 5:
                last_moved_piece, new_pos, original_pos = board.get_list_of_moves()[-1]

                # only if an enemy pawn moved 2 squares on the y axis
                if last_moved_piece.get_piece_color_and_type()[1] == PieceType.PAWN and abs(new_pos[1] - original_pos[1]) == 2:
                    # no need to check for an empty square
                    if new_pos[0] == x-1:
                        available_moves.append((x-1, 6))
                    if new_pos[0] == x+1:
                        available_moves.append((x+1, 6))

        if self.__color == PieceColor.BLACK:
            # works exactly the same as white
            # we will decrease y-coordinate instead
            if board.get_piece(x, y - 1).get_piece_color_and_type()[0] is None:
                available_moves.append((x, y - 1))

                # right at the beginning
                if y == 7 and board.get_piece(x, y - 2).get_piece_color_and_type()[0] is None:
                    available_moves.append((x, y - 2))

            if board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE:
                available_moves.append((x - 1, y - 1))
            if board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE:
                available_moves.append((x + 1, y - 1))

            # EN PASSANT ONLY
            if y == 4:
                last_moved_piece, new_pos, original_pos = board.get_list_of_moves()[-1]

                # only if an enemy pawn moved 2 squares on the y axis
                if last_moved_piece.get_piece_color_and_type()[1] == PieceType.PAWN and abs(new_pos[1] - original_pos[1]) == 2:
                    # also the square needs to be empty
                    if new_pos[0] == x - 1:
                        available_moves.append((x - 1, 3))
                    if new_pos[0] == x + 1:
                        available_moves.append((x + 1, 3))

        return available_moves

    def get_attacking_spots(self, board, x, y):

        # obs: No need to added the en passant attacking moves sine the pawn technically attacks that square
        attacking_spots = []

        if self.__color == PieceColor.WHITE:

            # it attacks the square if it's valid and empty or an opposite color piece
            # here's an example of why NotOnBoard is so useful
            # pawn only attack diagonally

            # LEFT
            if (board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or \
                    (board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y + 1))

            # RIGHT
            if board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK or \
                    (board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y + 1))

        elif self.__color == PieceColor.BLACK:

            # same as above

            # LEFT
            if (board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or \
                    (board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y - 1))

            # RIGHT
            if board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE or \
                    (board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y - 1))

        print(attacking_spots)

        return attacking_spots

    def __str__(self):
        return 'O'