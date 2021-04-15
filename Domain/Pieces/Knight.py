from Domain.Pieces.BoardPiece import *

class Knight(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_color_and_type(self):
        return self.__color, 'knight'

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece

        available_moves = []

        if self.__color == 'white':
            # check all 8 possibilities, add if opposite color or empty

            # two on the column
            if (board.get_piece(x + 2, y + 1).get_piece_color_and_type()[0] == 'black') or (
                    board.get_piece(x + 2, y + 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 2, y + 1))

            if (board.get_piece(x + 2, y - 1).get_piece_color_and_type()[0] == 'black') or (
                    board.get_piece(x + 2, y - 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 2, y - 1))

            if (board.get_piece(x - 2, y + 1).get_piece_color_and_type()[0] == 'black') or (
                    board.get_piece(x - 2, y + 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 2, y + 1))

            if (board.get_piece(x - 2, y - 1).get_piece_color_and_type()[0] == 'black') or (
                    board.get_piece(x - 2, y - 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 2, y - 1))

            # two on the line
            if (board.get_piece(x + 1, y + 2).get_piece_color_and_type()[0] == 'black') or (
                    board.get_piece(x + 1, y + 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 1, y + 2))

            if (board.get_piece(x + 1, y - 2).get_piece_color_and_type()[0] == 'black') or (
                    board.get_piece(x + 1, y - 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 1, y - 2))

            if (board.get_piece(x - 1, y + 2).get_piece_color_and_type()[0] == 'black') or (
                    board.get_piece(x - 1, y + 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 1, y + 2))

            if (board.get_piece(x - 1, y - 2).get_piece_color_and_type()[0] == 'black') or (
                    board.get_piece(x - 1, y - 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 1, y - 2))

        if self.__color == 'black':

            # same as above

            # two on the column
            if (board.get_piece(x + 2, y + 1).get_piece_color_and_type()[0] == 'white') or (
                    board.get_piece(x + 2, y + 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 2, y + 1))

            if (board.get_piece(x + 2, y - 1).get_piece_color_and_type()[0] == 'white') or (
                    board.get_piece(x + 2, y - 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 2, y - 1))

            if (board.get_piece(x - 2, y + 1).get_piece_color_and_type()[0] == 'white') or (
                    board.get_piece(x - 2, y + 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 2, y + 1))

            if (board.get_piece(x - 2, y - 1).get_piece_color_and_type()[0] == 'white') or (
                    board.get_piece(x - 2, y - 1).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 2, y - 1))

            # two on the line
            if (board.get_piece(x + 1, y + 2).get_piece_color_and_type()[0] == 'white') or (
                    board.get_piece(x + 1, y + 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 1, y + 2))

            if (board.get_piece(x + 1, y - 2).get_piece_color_and_type()[0] == 'white') or (
                    board.get_piece(x + 1, y - 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x + 1, y - 2))

            if (board.get_piece(x - 1, y + 2).get_piece_color_and_type()[0] == 'white') or (
                    board.get_piece(x - 1, y + 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 1, y + 2))

            if (board.get_piece(x - 1, y - 2).get_piece_color_and_type()[0] == 'white') or (
                    board.get_piece(x - 1, y - 2).get_piece_color_and_type()[0] is None):
                available_moves.append((x - 1, y - 2))
        return available_moves

    # Attacking spots are identical to available moves
    def get_attacking_spots(self, board, x, y):
        return self.get_available_moves(board, x, y)

    def __str__(self):
        return 'K'