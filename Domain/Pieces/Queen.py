from Domain.Pieces.BoardPiece import *
from Domain.PieceTypes.PieceType import PieceType
from Domain.PieceColors.PieceColor import PieceColor


class Queen(BoardPiece):
    def __init__(self, color: PieceColor):
        super().__init__()
        self.__color = color

    def get_piece_color_and_type(self):
        return self.__color, PieceType.QUEEN

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece

        # this acts like a bishop and a rock combined

        available_moves = []

        # bishop moves
        if self.__color == PieceColor.WHITE:

            # DIAGONALS
            # UP RIGHT
            for i in range(1, 8):

                if board.get_piece(x + i, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y + i))

                elif board.get_piece(x + i, y + i).get_piece_color_and_type()[0] == PieceColor.BLACK:
                    available_moves.append((x + i, y + i))
                    break

                else:
                    break

            # UP LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y + i))

                elif board.get_piece(x - i, y + i).get_piece_color_and_type()[0] == PieceColor.BLACK:
                    available_moves.append((x - i, y + i))
                    break

                else:
                    break

            # DOWN RIGHT
            for i in range(1, 8):
                if board.get_piece(x + i, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y - i))

                elif board.get_piece(x + i, y - i).get_piece_color_and_type()[0] == PieceColor.BLACK:
                    available_moves.append((x + i, y - i))
                    break

                else:
                    break

            # DOWN LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y - i))

                elif board.get_piece(x - i, y - i).get_piece_color_and_type()[0] == PieceColor.BLACK:
                    available_moves.append((x - i, y - i))
                    break

                else:
                    break

            # ROCK MOVES

            # UP
            for i in range(1, 8):
                if board.get_piece(x, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x, y + i))

                elif board.get_piece(x, y + i).get_piece_color_and_type()[0] == PieceColor.BLACK:
                    available_moves.append((x, y + i))
                    break

                else:
                    break

            # DOWN
            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x, y - i))

                elif board.get_piece(x, y - i).get_piece_color_and_type()[0] == PieceColor.BLACK:
                    available_moves.append((x, y - i))
                    break

                else:
                    break

            # RIGHT
            for i in range(1, 8):
                if board.get_piece(x + i, y).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y))

                elif board.get_piece(x + i, y).get_piece_color_and_type()[0] == PieceColor.BLACK:
                    available_moves.append((x + i, y))
                    break

                else:
                    break

            # LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y))

                elif board.get_piece(x - i, y).get_piece_color_and_type()[0] == PieceColor.BLACK:
                    available_moves.append((x - i, y))
                    break

                else:
                    break

        if self.__color == PieceColor.BLACK:

            # BISHOP MOVES

            # UP RIGHT
            for i in range(1, 8):
                if board.get_piece(x + i, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y + i))

                elif board.get_piece(x + i, y + i).get_piece_color_and_type()[0] == PieceColor.WHITE:
                    available_moves.append((x + i, y + i))
                    break

                else:
                    break

            # UP LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y + i))

                elif board.get_piece(x - i, y + i).get_piece_color_and_type()[0] == PieceColor.WHITE:
                    available_moves.append((x - i, y + i))
                    break

                else:
                    break

            # DOWN RIGHT
            for i in range(1, 8):
                if board.get_piece(x + i, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y - i))

                elif board.get_piece(x + i, y - i).get_piece_color_and_type()[0] == PieceColor.WHITE:
                    available_moves.append((x + i, y - i))
                    break

                else:
                    break

            # DOWN LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y - i))
                elif board.get_piece(x - i, y - i).get_piece_color_and_type()[0] == PieceColor.WHITE:
                    available_moves.append((x - i, y - i))
                    break
                else:
                    break

            # ROCK MOVES

            # UP
            for i in range(1, 8):
                if board.get_piece(x, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x, y + i))

                elif board.get_piece(x, y + i).get_piece_color_and_type()[0] == PieceColor.WHITE:
                    available_moves.append((x, y + i))
                    break

                else:
                    break

            # DOWN
            for i in range(1, 8):
                if board.get_piece(x, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x, y - i))

                elif board.get_piece(x, y - i).get_piece_color_and_type()[0] == PieceColor.WHITE:
                    available_moves.append((x, y - i))
                    break

                else:
                    break

            # RIGHT
            for i in range(1, 8):
                if board.get_piece(x + i, y).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y))

                elif board.get_piece(x + i, y).get_piece_color_and_type()[0] == PieceColor.WHITE:
                    available_moves.append((x + i, y))
                    break

                else:
                    break

            # LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y))

                elif board.get_piece(x - i, y).get_piece_color_and_type()[0] == PieceColor.WHITE:
                    available_moves.append((x - i, y))
                    break

                else:
                    break
        return available_moves

    def get_attacking_spots(self, board, x, y):
        return self.get_available_moves(board, x, y)

    def __str__(self):
        return 'Q'