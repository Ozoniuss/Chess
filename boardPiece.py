# black pieces
#
#
# white pieces --> the x axis
import sys
from termcolor import colored


class BoardPiece:
    def __init__(self):
        pass

    def get_piece_info(self):
        return None, None

    def get_available_moves(self, board, x, y):
        return []

    def __str__(self):
        return '.'


class NotOnBoard(BoardPiece):
    def __init__(self):
        super().__init__()

    def get_piece_info(self):
        return 'invalid', 'invalid'

    def __str__(self):
        return '.'


class Pawn(BoardPiece):
    # color('red' or 'blue') is the color of the pawn
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'pawn'

    def get_available_moves(self, board, x, y):
        available_moves = []

        if self.__color == 'blue':
            # right in front
            # if there's a piece ahead no moves (including beginning)
            # no need to check if valid because we'll never have a pawn on the last row
            if board.get_piece(x, y + 1).get_piece_info()[0] is None:
                available_moves.append((x, y + 1))
                # right at the beginning
                if y == 2 and board.get_piece(x, y + 2).get_piece_info()[0] is None:
                    available_moves.append((x, y + 2))

            # it can move on the side if there's a white piece
            # no need to check if valid here
            if board.get_piece(x - 1, y + 1).get_piece_info()[0] == 'red':
                available_moves.append((x - 1, y + 1))
            if board.get_piece(x + 1, y + 1).get_piece_info()[0] == 'red':
                available_moves.append((x + 1, y + 1))

        if self.__color == 'red':
            # right in front
            # if there's a piece ahead no moves (including beginning)
            # no need to check if valid because we'll never have a pawn on the last row
            if board.get_piece(x, y - 1).get_piece_info()[0] is None:
                available_moves.append((x, y - 1))
                # right at the beginning
                if y == 2 and board.get_piece(x, y - 2).get_piece_info()[0] is None:
                    available_moves.append((x, y - 2))

            # it can move on the side if there's a white piece
            # no need to check if valid here
            if board.get_piece(x - 1, y - 1).get_piece_info()[0] == 'red':
                available_moves.append((x - 1, y - 1))
            if board.get_piece(x + 1, y - 1).get_piece_info()[0] == 'red':
                available_moves.append((x + 1, y - 1))

        # still need to do the en passant

    def __str__(self):
        return colored('O', self.__color)


class Bishop(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'bishop'

    def get_available_moves(self, board, x, y):

        available_moves = []

        if self.__color == 'blue':

            # treat each of the diagonal cases.
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y + i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'red':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'red':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'red':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'red':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

        if self.__color == 'red':

            # treat each of the diagonal cases.
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y + i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'blue':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'blue':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'blue':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'blue':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

    def __str__(self):
        return colored('B', self.__color)


class Knight(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'knight'

    def get_available_moves(self, board, x, y):

        available_moves = []

        if self.__color == 'blue':
            # check all 8 possibilities, add if opposite color or empty

            # two on the column
            if (board.get_piece(x + 2, y + 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x + 2, y + 1).get_piece_info()[0] is None):
                available_moves.append((x + 2, y + 1))

            if (board.get_piece(x + 2, y - 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x + 2, y - 1).get_piece_info()[0] is None):
                available_moves.append((x + 2, y - 1))

            if (board.get_piece(x - 2, y + 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x - 2, y + 1).get_piece_info()[0] is None):
                available_moves.append((x - 2, y + 1))

            if (board.get_piece(x - 2, y - 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x - 2, y - 1).get_piece_info()[0] is None):
                available_moves.append((x - 2, y - 1))


            # two on the line
            if (board.get_piece(x + 1, y + 2).get_piece_info()[0] == 'red') or (
                    board.get_piece(x + 1, y + 2).get_piece_info()[0] is None):
                available_moves.append((x + 1, y + 2))

            if (board.get_piece(x + 1, y - 2).get_piece_info()[0] == 'red') or (
                    board.get_piece(x + 1, y - 2).get_piece_info()[0] is None):
                available_moves.append((x + 1, y - 2))

            if (board.get_piece(x - 1, y + 2).get_piece_info()[0] == 'red') or (
                    board.get_piece(x - 1, y + 2).get_piece_info()[0] is None):
                available_moves.append((x - 1, y + 2))

            if (board.get_piece(x - 1, y - 2).get_piece_info()[0] == 'red') or (
                    board.get_piece(x - 1, y - 2).get_piece_info()[0] is None):
                available_moves.append((x - 1, y - 2))

        if self.__color == 'red':

            # two on the column
            if (board.get_piece(x + 2, y + 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x + 2, y + 1).get_piece_info()[0] is None):
                available_moves.append((x + 2, y + 1))

            if (board.get_piece(x + 2, y - 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x + 2, y - 1).get_piece_info()[0] is None):
                available_moves.append((x + 2, y - 1))

            if (board.get_piece(x - 2, y + 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x - 2, y + 1).get_piece_info()[0] is None):
                available_moves.append((x - 2, y + 1))

            if (board.get_piece(x - 2, y - 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x - 2, y - 1).get_piece_info()[0] is None):
                available_moves.append((x - 2, y - 1))

            # two on the line
            if (board.get_piece(x + 1, y + 2).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x + 1, y + 2).get_piece_info()[0] is None):
                available_moves.append((x + 1, y + 2))

            if (board.get_piece(x + 1, y - 2).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x + 1, y - 2).get_piece_info()[0] is None):
                available_moves.append((x + 1, y - 2))

            if (board.get_piece(x - 1, y + 2).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x - 1, y + 2).get_piece_info()[0] is None):
                available_moves.append((x - 1, y + 2))

            if (board.get_piece(x - 1, y - 2).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x - 1, y - 2).get_piece_info()[0] is None):
                available_moves.append((x - 1, y - 2))

    def __str__(self):
        return colored('K', self.__color)


class Rock(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'rock'

    def get_available_moves(self, board, x, y):

        available_moves = []

        if self.__color == 'blue':

            # treat each of the possible lines
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x, y + i).get_piece_info()[0] is None:
                    available_moves.append((x, y + i))
                # if it's of opposite color add it (doesn't matter if king is added) and break
                elif board.get_piece(x, y + i).get_piece_info()[0] == 'red':
                    available_moves.append((x, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_info()[0] is None:
                    available_moves.append((x, y - i))
                elif board.get_piece(x, y - i).get_piece_info()[0] == 'red':
                    available_moves.append((x, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y).get_piece_info()[0] is None:
                    available_moves.append((x + i, y))
                elif board.get_piece(x + i, y).get_piece_info()[0] == 'red':
                    available_moves.append((x + i, y))
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y).get_piece_info()[0] is None:
                    available_moves.append((x - i, y))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y).get_piece_info()[0] == 'red':
                    available_moves.append((x - i, y))
                # if it's invalid or of the same color neglect it
                else:
                    break

        if self.__color == 'red':

            # treat each of the possible lines
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x, y + i).get_piece_info()[0] is None:
                    available_moves.append((x, y + i))
                # if it's of opposite color add it (doesn't matter if king is added) and break
                elif board.get_piece(x, y + i).get_piece_info()[0] == 'blue':
                    available_moves.append((x, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_info()[0] is None:
                    available_moves.append((x, y - i))
                elif board.get_piece(x, y - i).get_piece_info()[0] == 'blue':
                    available_moves.append((x, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y).get_piece_info()[0] is None:
                    available_moves.append((x + i, y))
                elif board.get_piece(x + i, y).get_piece_info()[0] == 'blue':
                    available_moves.append((x + i, y))
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y).get_piece_info()[0] is None:
                    available_moves.append((x - i, y))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y).get_piece_info()[0] == 'blue':
                    available_moves.append((x - i, y))
                # if it's invalid or of the same color neglect it
                else:
                    break

            # treat each of the diagonal cases.
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y + i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'blue':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'blue':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'blue':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'blue':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

    def __str__(self):
        return colored('R', self.__color)


class Queen(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'queen'

    def get_available_moves(self, board, x, y):

        # we'll combine what we did at the bishop and the rock

        available_moves = []

        # rock moves
        if self.__color == 'blue':

            # treat each of the possible lines
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x, y + i).get_piece_info()[0] is None:
                    available_moves.append((x, y + i))
                # if it's of opposite color add it (doesn't matter if king is added) and break
                elif board.get_piece(x, y + i).get_piece_info()[0] == 'red':
                    available_moves.append((x, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_info()[0] is None:
                    available_moves.append((x, y - i))
                elif board.get_piece(x, y - i).get_piece_info()[0] == 'red':
                    available_moves.append((x, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y).get_piece_info()[0] is None:
                    available_moves.append((x + i, y))
                elif board.get_piece(x + i, y).get_piece_info()[0] == 'red':
                    available_moves.append((x + i, y))
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y).get_piece_info()[0] is None:
                    available_moves.append((x - i, y))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y).get_piece_info()[0] == 'red':
                    available_moves.append((x - i, y))
                # if it's invalid or of the same color neglect it
                else:
                    break

            # bishop moves.
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y + i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'red':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'red':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'red':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'red':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

        elif self.__color == 'red':

            # rock moves
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x, y + i).get_piece_info()[0] is None:
                    available_moves.append((x, y + i))
                # if it's of opposite color add it (doesn't matter if king is added) and break
                elif board.get_piece(x, y + i).get_piece_info()[0] == 'blue':
                    available_moves.append((x, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_info()[0] is None:
                    available_moves.append((x, y - i))
                elif board.get_piece(x, y - i).get_piece_info()[0] == 'blue':
                    available_moves.append((x, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y).get_piece_info()[0] is None:
                    available_moves.append((x + i, y))
                elif board.get_piece(x + i, y).get_piece_info()[0] == 'blue':
                    available_moves.append((x + i, y))
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y).get_piece_info()[0] is None:
                    available_moves.append((x - i, y))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y).get_piece_info()[0] == 'blue':
                    available_moves.append((x - i, y))
                # if it's invalid or of the same color neglect it
                else:
                    break

            # bishop moves
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y + i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'blue':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'blue':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'blue':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'blue':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break



    def __str__(self):
        return colored('Q', self.__color)


class King(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'king'

    def get_available_moves(self, board, x, y):
        available_moves = []

        if self.__color == 'blue':

            if (board.get_piece(x, y + 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x, y + 1):
                    available_moves.append((x, y + 1))

            if (board.get_piece(x, y - 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x, y - 1):
                    available_moves.append((x, y - 1))

            if (board.get_piece(x - 1, y).get_piece_info()[0] == 'red') or (
                    board.get_piece(x - 1, y).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y):
                    available_moves.append((x - 1, y))

            if (board.get_piece(x + 1, y).get_piece_info()[0] == 'red') or (
                    board.get_piece(x + 1, y).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y):
                    available_moves.append((x + 1, y))

            if (board.get_piece(x + 1, y + 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x + 1, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y + 1):
                    available_moves.append((x + 1, y + 1))

            if (board.get_piece(x + 1, y - 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x + 1, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y - 1):
                    available_moves.append((x + 1, y - 1))

            if (board.get_piece(x - 1, y + 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x - 1, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y + 1):
                    available_moves.append((x - 1, y + 1))

            if (board.get_piece(x - 1, y - 1).get_piece_info()[0] == 'red') or (
                    board.get_piece(x - 1, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y - 1):
                    available_moves.append((x - 1, y - 1))

        if self.__color == 'red':


            if (board.get_piece(x, y + 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x, y + 1):
                    available_moves.append((x, y + 1))

            if (board.get_piece(x, y - 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x, y - 1):
                    available_moves.append((x, y - 1))

            if (board.get_piece(x - 1, y).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x - 1, y).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y):
                    available_moves.append((x - 1, y))

            if (board.get_piece(x + 1, y).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x + 1, y).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y):
                    available_moves.append((x + 1, y))

            if (board.get_piece(x + 1, y + 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x + 1, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y + 1):
                    available_moves.append((x + 1, y + 1))

            if (board.get_piece(x + 1, y - 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x + 1, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y - 1):
                    available_moves.append((x + 1, y - 1))

            if (board.get_piece(x - 1, y + 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x - 1, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y + 1):
                    available_moves.append((x - 1, y + 1))

            if (board.get_piece(x - 1, y - 1).get_piece_info()[0] == 'blue') or (
                    board.get_piece(x - 1, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y - 1):
                    available_moves.append((x - 1, y - 1))

    def __str__(self):
        return colored('X', self.__color)

    def is_check(self, board, x, y):

        if self.__color == 'blue':
            for positions in board.get_table():
                # get the color of the piece at each position
                # we are only interested in opposite color pieces:
                piece = board.get_table()[positions]
                if piece.get_piece_info()[0] == 'red':
                    # get the positions the piece attacks
                    piece_moves = piece.get_available_moves(board, positions[0], positions[1])
                    if (x, y) in piece_moves:
                        return True
            return False

        if self.__color == 'red':
            for positions in board.get_table():
                # get the color of the piece at each position
                # we are only interested in opposite color pieces:
                piece = board.get_table()[positions]
                if piece.get_piece_info()[0] == 'blue':
                    # get the positions the piece attacks
                    piece_moves = piece.get_available_moves(board, positions[0], positions[1])
                    if (x, y) in piece_moves:
                        return True
            return False


    def is_stalemate(self):
        pass

    # for simplicity
    def is_checkmate(self):
        pass


