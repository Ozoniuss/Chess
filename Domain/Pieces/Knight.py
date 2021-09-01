from Domain.Pieces.BoardPiece import *
from Domain.PieceTypes.PieceType import PieceType
from Domain.PieceColors.PieceColor import PieceColor

class Knight(BoardPiece):
    def __init__(self, color: PieceColor):
        super().__init__()
        self.__color = color

    def get_piece_color_and_type(self):
        return self.__color, PieceType.KNIGHT

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece

        available_moves = []

        if self.__color == PieceColor.WHITE:
            # check all 8 possibilities, add if opposite color or empty

            # two on the column
            if (board.get_piece(x + 2, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 2, y + 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 2, y + 1))

            if (board.get_piece(x + 2, y - 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 2, y - 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 2, y - 1))

            if (board.get_piece(x - 2, y + 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 2, y + 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 2, y + 1))

            if (board.get_piece(x - 2, y - 1).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 2, y - 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 2, y - 1))

            # two on the line
            if (board.get_piece(x + 1, y + 2).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 1, y + 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 1, y + 2))

            if (board.get_piece(x + 1, y - 2).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x + 1, y - 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 1, y - 2))

            if (board.get_piece(x - 1, y + 2).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 1, y + 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 1, y + 2))

            if (board.get_piece(x - 1, y - 2).get_piece_color_and_type()[0] == PieceColor.BLACK) or (
                    board.get_piece(x - 1, y - 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 1, y - 2))

        if self.__color == PieceColor.BLACK:

            # same as above

            # two on the column
            if (board.get_piece(x + 2, y + 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 2, y + 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 2, y + 1))

            if (board.get_piece(x + 2, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 2, y - 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 2, y - 1))

            if (board.get_piece(x - 2, y + 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 2, y + 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 2, y + 1))

            if (board.get_piece(x - 2, y - 1).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 2, y - 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 2, y - 1))

            # two on the line
            if (board.get_piece(x + 1, y + 2).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 1, y + 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 1, y + 2))

            if (board.get_piece(x + 1, y - 2).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x + 1, y - 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 1, y - 2))

            if (board.get_piece(x - 1, y + 2).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 1, y + 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 1, y + 2))

            if (board.get_piece(x - 1, y - 2).get_piece_color_and_type()[0] == PieceColor.WHITE) or (
                    board.get_piece(x - 1, y - 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 1, y - 2))
        return available_moves

    # Attacking spots are identical to available moves
    def get_attacking_spots(self, board, x, y):
        return self.get_available_moves(board, x, y)

    def __str__(self):
        return 'K'