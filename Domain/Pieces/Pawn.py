from Domain.Pieces.BoardPiece import *

class Pawn(BoardPiece):
    # color('red' or 'white') is the color of the pawn
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_color_and_type(self):
        return self.__color, 'pawn'

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece
        available_moves = []

        if self.__color == 'white':
            # right in front
            # if there's a piece ahead there are no moves in front (including beginning)
            # no need to check if valid because we'll never have a pawn on the last row
            #     since it will modify to a different piece

            if board.get_piece(x, y + 1).get_piece_color_and_type()[0] is None:
                available_moves.append((x, y + 1))

                # right at the beginning
                if y == 2 and board.get_piece(x, y + 2).get_piece_color_and_type()[0] is None:
                    available_moves.append((x, y + 2))

            # it can move on the side if there's a white piece
            # no need to check if valid here since it's obviously valid
            if board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] == 'black':
                available_moves.append((x - 1, y + 1))
            if board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] == 'black':
                available_moves.append((x + 1, y + 1))

        if self.__color == 'black':
            # works exactly the same as white
            # we will decrease y-coordinate instead
            if board.get_piece(x, y - 1).get_piece_color_and_type()[0] is None:
                available_moves.append((x, y - 1))

                # right at the beginning
                if y == 7 and board.get_piece(x, y - 2).get_piece_color_and_type()[0] is None:
                    available_moves.append((x, y - 2))

            if board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] == 'white':
                available_moves.append((x - 1, y - 1))
            if board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] == 'white':
                available_moves.append((x + 1, y - 1))

        # STILL NEED TO EN PASSANT
        return available_moves

    def get_attacking_spots(self, board, x, y):

        attacking_spots = []

        if self.__color == 'white':

            # it attacks the square if it's valid and empty or an opposite color piece
            # here's an example of why NotOnBoard is so useful
            # pawn only attack diagonally

            # LEFT
            if (board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] == 'black') or \
                    (board.get_piece(x - 1, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y + 1))

            # RIGHT
            if board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] == 'black' or \
                    (board.get_piece(x + 1, y + 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y + 1))


        elif self.__color == 'black':

            # same as avove

            #LEFT
            if (board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] == 'white') or \
                    (board.get_piece(x - 1, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x - 1, y - 1))

            #RIGHT
            if board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] == 'white' or \
                    (board.get_piece(x + 1, y - 1).get_piece_color_and_type()[0] is None):
                attacking_spots.append((x + 1, y - 1))

        print(attacking_spots)

        return attacking_spots

    def __str__(self):
        return 'O'