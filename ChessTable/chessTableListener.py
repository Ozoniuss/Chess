from ChessTable.chessTable import *

import ChessTable
from Event.Events import *
from typing import *

def handle_GUI_move(chesstable: ChessTable, x, y, new_x, new_y, promotion_piece=EmptyPiece()):
    chesstable.move_piece(x, y, new_x, new_y, promotion_piece)

subscribe('GUI_moved', handle_GUI_move)
