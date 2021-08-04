from enum import Enum, auto

class PieceType(Enum):

    PAWN = auto()
    KNIGHT = auto()
    BISHOP = auto()
    ROCK = auto()
    QUEEN = auto()
    KING = auto()
    EMPTY_SQUARE = auto()
    NOT_ON_BOARD = auto()

