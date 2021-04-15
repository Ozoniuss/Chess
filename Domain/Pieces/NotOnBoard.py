from Domain.Pieces.BoardPiece import BoardPiece

class NotOnBoard(BoardPiece):
    def __init__(self):
        super().__init__()

    def get_piece_info(self) -> tuple:
        return 'invalid', 'invalid'

    def __str__(self):
        return '.'