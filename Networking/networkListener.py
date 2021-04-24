from Networking.network import *
from Event.Events import *
from ChessTable.chessTable import ChessTable
import pickle

def handle_notify_server(client: Client, table : ChessTable, x,y, new_x, new_y, promotion_piece):
    data = SECRET_MESSAGE + str([x,y,new_x, new_y, promotion_piece.get_piece_color_and_type()])
    client.send(data)


subscribe('Notify_server', handle_notify_server)