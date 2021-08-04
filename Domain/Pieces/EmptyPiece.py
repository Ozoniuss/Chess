from Domain.Pieces.BoardPiece import *

class EmptyPiece(BoardPiece):

    def get_piece_color_and_type(self) -> tuple:
        return None, None

    def get_available_moves(self, board, x, y) -> list:
        return []

    def __str__(self):
        return '.'
