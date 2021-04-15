from abc import ABC, abstractmethod

# this is an interface for all the chess pieces

class BoardPiece(ABC):

    @abstractmethod
    def get_piece_info(self) -> tuple:
        return None, None

    def get_available_moves(self, board, x, y) -> list[tuple]:
        return []

    def __str__(self):
        return '.'

