from GUI.GUI_improved import *
from ChessTable.chessTableListener import *
from ChessTable.chessTable import ChessTable

table = ChessTable()
root = Tk()
interface = GUI(table, root)
interface.run_game()
root.mainloop()
