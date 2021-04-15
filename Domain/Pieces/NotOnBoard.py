from Domain.Pieces.BoardPiece import BoardPiece

class NotOnBoard(BoardPiece):
    def __init__(self):
        super().__init__()

    def get_piece_color_and_type(self) -> tuple:
        return 'invalid', 'invalid'

    def get_available_moves(self, board, x, y) -> list:
        return []

    def __str__(self):
        return '.'