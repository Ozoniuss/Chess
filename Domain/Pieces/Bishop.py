from Domain.Pieces.BoardPiece import *

class Bishop(BoardPiece):
    def __init__(self, color):
        super().__init__()
        self.__color = color

    def get_piece_color_and_type(self):
        return self.__color, 'bishop'

    def get_available_moves(self, board, x, y):
        # the board is passed as a parameter
        # x, y represent the coordinates of the piece

        available_moves = []

        if self.__color == 'white':

            # DIAGONALS

            # UP RIGHT
            for i in range(1, 8):

                if board.get_piece(x + i, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y + i))

                elif board.get_piece(x + i, y + i).get_piece_color_and_type()[0] == 'black':
                    available_moves.append((x + i, y + i))
                    break

                else:
                    break

            # UP LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y + i))

                elif board.get_piece(x - i, y + i).get_piece_color_and_type()[0] == 'black':
                    available_moves.append((x - i, y + i))
                    break

                else:
                    break

            # DOWN RIGHT
            for i in range(1, 8):
                if board.get_piece(x + i, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y - i))

                elif board.get_piece(x + i, y - i).get_piece_color_and_type()[0] == 'black':
                    available_moves.append((x + i, y - i))
                    break

                else:
                    break

            # DOWN LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y - i))

                elif board.get_piece(x - i, y - i).get_piece_color_and_type()[0] == 'black':
                    available_moves.append((x - i, y - i))
                    break

                else:
                    break

        if self.__color == 'black':

            # Treat identically as above

            # UP RIGHT
            for i in range(1, 8):
                if board.get_piece(x + i, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y + i))

                elif board.get_piece(x + i, y + i).get_piece_color_and_type()[0] == 'white':
                    available_moves.append((x + i, y + i))
                    break

                else:
                    break


            # UP LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y + i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y + i))

                elif board.get_piece(x - i, y + i).get_piece_color_and_type()[0] == 'white':
                    available_moves.append((x - i, y + i))
                    break

                else:
                    break

            # DOWN RIGHT
            for i in range(1, 8):
                if board.get_piece(x + i, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x + i, y - i))

                elif board.get_piece(x + i, y - i).get_piece_color_and_type()[0] == 'white':
                    available_moves.append((x + i, y - i))
                    break

                else:
                    break

            # DOWN LEFT
            for i in range(1, 8):
                if board.get_piece(x - i, y - i).get_piece_color_and_type()[0] is None:
                    available_moves.append((x - i, y - i))
                elif board.get_piece(x - i, y - i).get_piece_color_and_type()[0] == 'white':
                    available_moves.append((x - i, y - i))
                    break
                else:
                    break
        return available_moves

    # Attacking spots are identical to available moves
    def get_attacking_spots(self, board, x, y):
        return self.get_available_moves(board, x, y)

    def __str__(self):
        return 'B'