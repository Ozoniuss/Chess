from abc import ABC, abstractmethod

# This acts like a template for all the pieces
# There are Pawns, Bishops, Knights, Rocks, Queens and Kings
# NotOnBoard is a class used to designate an invalid piece -- it is useful when
#    a move is made outside the board


class BoardPiece(ABC):

    @abstractmethod
    def get_piece_color_and_type(self) -> tuple : pass

    @abstractmethod
    def get_available_moves(self, board, x, y) -> list: pass


