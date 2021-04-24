from Networking.network import *
from Networking.server import n
from ChessTable.chessTableListener import *
from Networking.networkListener import *
from GUI.GUI_improved import *

# root.mainloop()



table = ChessTable()
root = Tk()
# interface = GUI(table, root, c)
# interface.run_game()
c = Client(n)
c.connect_to_server()

c.start_receive_thread()
c.initialize_game_params(table, root)
c.run_game()