# black pieces
#
#
# white pieces --> the x axis

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
    # color('red' or 'white') is the color of the pawn
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'pawn'

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece
        available_moves = []

        if self.__color == 'white':
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
            if board.get_piece(x - 1, y + 1).get_piece_info()[0] == 'black':
                available_moves.append((x - 1, y + 1))
            if board.get_piece(x + 1, y + 1).get_piece_info()[0] == 'black':
                available_moves.append((x + 1, y + 1))

        if self.__color == 'black':
            # right in front
            # if there's a piece ahead no moves (including beginning)
            # no need to check if valid because we'll never have a pawn on the last row
            if board.get_piece(x, y - 1).get_piece_info()[0] is None:
                available_moves.append((x, y - 1))
                # right at the beginning
                if y == 7 and board.get_piece(x, y - 2).get_piece_info()[0] is None:
                    available_moves.append((x, y - 2))


            # it can move on the side if there's a white piece
            # no need to check if valid here
            if board.get_piece(x - 1, y - 1).get_piece_info()[0] == 'white':
                available_moves.append((x - 1, y - 1))
            if board.get_piece(x + 1, y - 1).get_piece_info()[0] == 'white':
                available_moves.append((x + 1, y - 1))

        # still need to do the en passant
        print(available_moves)
        return available_moves

    def __str__(self):
        return 'O'


class Bishop(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'bishop'

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece

        available_moves = []

        if self.__color == 'white':

            # treat each of the diagonal cases.
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y + i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'black':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'black':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'black':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'black':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

        if self.__color == 'black':

            # treat each of the diagonal cases.
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y + i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'white':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'white':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'white':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'white':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break
        return available_moves

    def __str__(self):
        return 'B'


class Knight(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'knight'

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece

        available_moves = []

        if self.__color == 'white':
            # check all 8 possibilities, add if opposite color or empty

            # two on the column
            if (board.get_piece(x + 2, y + 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x + 2, y + 1).get_piece_info()[0] is None):
                available_moves.append((x + 2, y + 1))

            if (board.get_piece(x + 2, y - 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x + 2, y - 1).get_piece_info()[0] is None):
                available_moves.append((x + 2, y - 1))

            if (board.get_piece(x - 2, y + 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x - 2, y + 1).get_piece_info()[0] is None):
                available_moves.append((x - 2, y + 1))

            if (board.get_piece(x - 2, y - 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x - 2, y - 1).get_piece_info()[0] is None):
                available_moves.append((x - 2, y - 1))

            # two on the line
            if (board.get_piece(x + 1, y + 2).get_piece_info()[0] == 'black') or (
                    board.get_piece(x + 1, y + 2).get_piece_info()[0] is None):
                available_moves.append((x + 1, y + 2))

            if (board.get_piece(x + 1, y - 2).get_piece_info()[0] == 'black') or (
                    board.get_piece(x + 1, y - 2).get_piece_info()[0] is None):
                available_moves.append((x + 1, y - 2))

            if (board.get_piece(x - 1, y + 2).get_piece_info()[0] == 'black') or (
                    board.get_piece(x - 1, y + 2).get_piece_info()[0] is None):
                available_moves.append((x - 1, y + 2))

            if (board.get_piece(x - 1, y - 2).get_piece_info()[0] == 'black') or (
                    board.get_piece(x - 1, y - 2).get_piece_info()[0] is None):
                available_moves.append((x - 1, y - 2))

        if self.__color == 'black':

            # two on the column
            if (board.get_piece(x + 2, y + 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x + 2, y + 1).get_piece_info()[0] is None):
                available_moves.append((x + 2, y + 1))

            if (board.get_piece(x + 2, y - 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x + 2, y - 1).get_piece_info()[0] is None):
                available_moves.append((x + 2, y - 1))

            if (board.get_piece(x - 2, y + 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x - 2, y + 1).get_piece_info()[0] is None):
                available_moves.append((x - 2, y + 1))

            if (board.get_piece(x - 2, y - 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x - 2, y - 1).get_piece_info()[0] is None):
                available_moves.append((x - 2, y - 1))

            # two on the line
            if (board.get_piece(x + 1, y + 2).get_piece_info()[0] == 'white') or (
                    board.get_piece(x + 1, y + 2).get_piece_info()[0] is None):
                available_moves.append((x + 1, y + 2))

            if (board.get_piece(x + 1, y - 2).get_piece_info()[0] == 'white') or (
                    board.get_piece(x + 1, y - 2).get_piece_info()[0] is None):
                available_moves.append((x + 1, y - 2))

            if (board.get_piece(x - 1, y + 2).get_piece_info()[0] == 'white') or (
                    board.get_piece(x - 1, y + 2).get_piece_info()[0] is None):
                available_moves.append((x - 1, y + 2))

            if (board.get_piece(x - 1, y - 2).get_piece_info()[0] == 'white') or (
                    board.get_piece(x - 1, y - 2).get_piece_info()[0] is None):
                available_moves.append((x - 1, y - 2))
        return available_moves

    def __str__(self):
        return 'K'


class Rock(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'rock'

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece

        available_moves = []

        if self.__color == 'white':

            # treat each of the possible lines
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x, y + i).get_piece_info()[0] is None:
                    available_moves.append((x, y + i))
                # if it's of opposite color add it (doesn't matter if king is added) and break
                elif board.get_piece(x, y + i).get_piece_info()[0] == 'black':
                    available_moves.append((x, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_info()[0] is None:
                    available_moves.append((x, y - i))
                elif board.get_piece(x, y - i).get_piece_info()[0] == 'black':
                    available_moves.append((x, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y).get_piece_info()[0] is None:
                    available_moves.append((x + i, y))
                elif board.get_piece(x + i, y).get_piece_info()[0] == 'black':
                    available_moves.append((x + i, y))
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y).get_piece_info()[0] is None:
                    available_moves.append((x - i, y))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y).get_piece_info()[0] == 'black':
                    available_moves.append((x - i, y))
                # if it's invalid or of the same color neglect it
                else:
                    break

        if self.__color == 'black':

            # treat each of the possible lines
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x, y + i).get_piece_info()[0] is None:
                    available_moves.append((x, y + i))
                # if it's of opposite color add it (doesn't matter if king is added) and break
                elif board.get_piece(x, y + i).get_piece_info()[0] == 'white':
                    available_moves.append((x, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_info()[0] is None:
                    available_moves.append((x, y - i))
                elif board.get_piece(x, y - i).get_piece_info()[0] == 'white':
                    available_moves.append((x, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y).get_piece_info()[0] is None:
                    available_moves.append((x + i, y))
                elif board.get_piece(x + i, y).get_piece_info()[0] == 'white':
                    available_moves.append((x + i, y))
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y).get_piece_info()[0] is None:
                    available_moves.append((x - i, y))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y).get_piece_info()[0] == 'white':
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
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'white':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'white':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'white':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'white':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break
        return available_moves

    def __str__(self):
        return 'R'


class Queen(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'queen'

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece

        # we'll combine what we did at the bishop and the rock

        available_moves = []

        # rock moves
        if self.__color == 'white':

            # treat each of the possible lines
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x, y + i).get_piece_info()[0] is None:
                    available_moves.append((x, y + i))
                # if it's of opposite color add it (doesn't matter if king is added) and break
                elif board.get_piece(x, y + i).get_piece_info()[0] == 'black':
                    available_moves.append((x, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_info()[0] is None:
                    available_moves.append((x, y - i))
                elif board.get_piece(x, y - i).get_piece_info()[0] == 'black':
                    available_moves.append((x, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y).get_piece_info()[0] is None:
                    available_moves.append((x + i, y))
                elif board.get_piece(x + i, y).get_piece_info()[0] == 'black':
                    available_moves.append((x + i, y))
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y).get_piece_info()[0] is None:
                    available_moves.append((x - i, y))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y).get_piece_info()[0] == 'black':
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
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'black':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'black':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'black':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'black':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

        elif self.__color == 'black':

            # rock moves
            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x, y + i).get_piece_info()[0] is None:
                    available_moves.append((x, y + i))
                # if it's of opposite color add it (doesn't matter if king is added) and break
                elif board.get_piece(x, y + i).get_piece_info()[0] == 'white':
                    available_moves.append((x, y + i))
                    break
                # if it's invalid or of the same color neglect it then break
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_info()[0] is None:
                    available_moves.append((x, y - i))
                elif board.get_piece(x, y - i).get_piece_info()[0] == 'white':
                    available_moves.append((x, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y).get_piece_info()[0] is None:
                    available_moves.append((x + i, y))
                elif board.get_piece(x + i, y).get_piece_info()[0] == 'white':
                    available_moves.append((x + i, y))
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y).get_piece_info()[0] is None:
                    available_moves.append((x - i, y))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y).get_piece_info()[0] == 'white':
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
                elif board.get_piece(x + i, y + i).get_piece_info()[0] == 'white':
                    available_moves.append((x + i, y + i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break

            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y + i))
                elif board.get_piece(x - i, y + i).get_piece_info()[0] == 'white':
                    available_moves.append((x - i, y + i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x + i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x + i, y - i))
                elif board.get_piece(x + i, y - i).get_piece_info()[0] == 'white':
                    available_moves.append((x + i, y - i))
                    break
                else:
                    break

            for i in range(1, 8):
                # if it's empty clearly add it
                if board.get_piece(x - i, y - i).get_piece_info()[0] is None:
                    available_moves.append((x - i, y - i))
                # if it's of opposite color add it (doesn't matter if king is added)
                elif board.get_piece(x - i, y - i).get_piece_info()[0] == 'white':
                    available_moves.append((x - i, y - i))
                    break
                # if it's invalid or of the same color neglect it
                else:
                    break
        return available_moves

    def __str__(self):
        return 'Q'


class King(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_info(self):
        return self.__color, 'king'

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece
        # will not include positions where the king is in check

        available_moves = []

        # for the moment we remove the king to avoid glitches, like the old position of the king
        # being in the path of an attack
        # board.get_table[(x, y)] = BoardPiece()

        if self.__color == 'white':

            if (board.get_piece(x, y + 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x, y + 1).get_piece_info()[0] is None):

                if not self.is_check(board, x, y + 1):
                    available_moves.append((x, y + 1))

            if (board.get_piece(x, y - 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x, y - 1):
                    available_moves.append((x, y - 1))

            if (board.get_piece(x - 1, y).get_piece_info()[0] == 'black') or (
                    board.get_piece(x - 1, y).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y):
                    available_moves.append((x - 1, y))

            if (board.get_piece(x + 1, y).get_piece_info()[0] == 'black') or (
                    board.get_piece(x + 1, y).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y):
                    available_moves.append((x + 1, y))

            if (board.get_piece(x + 1, y + 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x + 1, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y + 1):
                    available_moves.append((x + 1, y + 1))

            if (board.get_piece(x + 1, y - 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x + 1, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y - 1):
                    available_moves.append((x + 1, y - 1))

            if (board.get_piece(x - 1, y + 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x - 1, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y + 1):
                    available_moves.append((x - 1, y + 1))

            if (board.get_piece(x - 1, y - 1).get_piece_info()[0] == 'black') or (
                    board.get_piece(x - 1, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y - 1):
                    available_moves.append((x - 1, y - 1))

            board.get_table[(x, y)] = King('white') # place the king back

        if self.__color == 'black':


            if (board.get_piece(x, y + 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x, y + 1):
                    available_moves.append((x, y + 1))

            if (board.get_piece(x, y - 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x, y - 1):
                    available_moves.append((x, y - 1))

            if (board.get_piece(x - 1, y).get_piece_info()[0] == 'white') or (
                    board.get_piece(x - 1, y).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y):
                    available_moves.append((x - 1, y))

            if (board.get_piece(x + 1, y).get_piece_info()[0] == 'white') or (
                    board.get_piece(x + 1, y).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y):
                    available_moves.append((x + 1, y))

            if (board.get_piece(x + 1, y + 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x + 1, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y + 1):
                    available_moves.append((x + 1, y + 1))

            if (board.get_piece(x + 1, y - 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x + 1, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x + 1, y - 1):
                    available_moves.append((x + 1, y - 1))

            if (board.get_piece(x - 1, y + 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x - 1, y + 1).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y + 1):
                    available_moves.append((x - 1, y + 1))

            if (board.get_piece(x - 1, y - 1).get_piece_info()[0] == 'white') or (
                    board.get_piece(x - 1, y - 1).get_piece_info()[0] is None):
                if not self.is_check(board, x - 1, y - 1):
                    available_moves.append((x - 1, y - 1))

            board.get_table[(x, y)] = King('black')  # place the king back

        return available_moves

    def __str__(self):
        return 'X'

    def is_check(self, board, x, y):
        # the king is at position x, y. Returns true if the king is in check.

        if self.__color == 'white':
            for positions in board.get_table():
                # get the color of the piece at each position
                # we are only interested in opposite color pieces:
                piece = board.get_table()[positions]
                if piece.get_piece_info()[0] == 'black':
                    # get the positions the piece attacks
                    piece_moves = piece.get_available_moves(board, positions[0], positions[1])
                    if (x, y) in piece_moves:
                        return True
            return False

        if self.__color == 'black':
            for positions in board.get_table():
                # get the color of the piece at each position
                # we are only interested in opposite color pieces:
                piece = board.get_table()[positions]
                if piece.get_piece_info()[0] == 'white':
                    # get the positions the piece attacks
                    piece_moves = piece.get_available_moves(board, positions[0], positions[1])
                    if (x, y) in piece_moves:
                        return True
            return False




    # def is_stalemate(self, board, x, y):
    #     # no available positions and no check
    #     if (self.get_available_moves(board, x, y) == []) and (self.is_check(board, x, y) == False):
    #         return True
    #     return False
    #
    # # for simplicity
    # def is_checkmate(self):
    #     pass
    #

