from GUI_improved import *

table = ChessTable()
root = Tk()
interface = GUI(table, root)
interface.run_game()
root.mainloop()
