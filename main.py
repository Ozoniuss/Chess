from tkinter import *
from chessTable import ChessTable

class GUI:
    def __init__(self, table, master):
        self.__table = table
        self.__frame = Frame(master,  width=870, height=750)
        self.__frame.pack(expand=True)
        self.__frame.grid_propagate(0)
        self.__colors = {'board1' : 'mint cream',
                         'board2' : 'DarkSlateGray4',
                         'when clicked': 'SkyBlue3',
                         'available position': 'gray71'
                        }
        self.__square_dict = {}
        self.__pieces_dict = {}
        self.__canvas = Canvas(self.__frame, width=700, height=700, highlightthickness=0)
        self.__changes = []

    # def convert_board_to_interface(self):
    #     self.__table.populate_chess_table()
    #     for row in range(8,0,-1):
    #         for column in range(1, 9):
    #             square = Button(self.__frame, width=10, height=5)
    #             canvas = Canvas(square, width=80, height=80, highlightthickness=0, relief='ridge')
    #             if (row + column)%2 == 0:
    #                 square.config(bg=self.__colors['board1'])
    #                 canvas.config(bg=self.__colors['board1'])
    #             else:
    #                 square.config(bg=self.__colors['board2'])
    #                 canvas.config(bg=self.__colors['board2'])
    #             if column == 1:
    #                 canvas.create_text(1,1, text=str(row), anchor=NW)
    #             if row == 1:
    #                 canvas.create_text(80,80, text=chr(ord('A')+column-1), anchor = SE)
    #
    #             square.grid(row=9-row, column=column)
    #             canvas.grid(row=9-row, column=column)
    #             canvas.bind('<B1-Motion>', self.click_handler)
    #             self.add_piece(canvas, row, column)
    #
    #             self.__canvas_dict[(9-row, column)] = canvas
    #             self.__button_dict[(9 - row, column)] = square

    def convert_board_to_interface(self):
        self.__table.populate_chess_table()
        for x in range(1,9):
            for y in range(8,0,-1):
                square = self.__canvas.create_rectangle((x-1)*80, (9-y-1)*80, x*80, (9-y)*80)
                self.__square_dict[(x,y)] = square
                if(x+y)%2 == 0:
                    self.__canvas.itemconfig(square, fill = self.__colors['board1'])
                else:
                    self.__canvas.itemconfig(square, fill = self.__colors['board2'])
                self.add_piece(self.__canvas, x, y)
                if x == 1:
                    self.__canvas.create_text((x-1)*80 + 10 ,(9-y-1)*80 + 10, text=str(y))
                if y == 1:
                    self.__canvas.create_text(x*80 - 10, (9-y)*80 - 10, text=chr(ord('A')+x-1))
        self.__canvas.pack()
        self.__canvas.bind('<Button-1>', self.click_handler)

    def click_handler(self, event):
        x = event.x//80 + 1
        y = 8 - event.y//80
        if x not in range(1,9) or y not in range(1,9):
            pass
        else:
            self.undo_click()
            square = self.__square_dict[(x,y)]
            self.__canvas.itemconfig(square, fill = self.__colors['when clicked'])
            self.__changes.append([square, x, y])
            piece = self.__table.get_piece(x, y)
            available_positions = piece.get_available_moves(self.__table, x, y)
            for position in available_positions:
                square = self.__square_dict[(position[0], position[1])]
                self.__canvas.itemconfig(square, fill=self.__colors['available position'])
                self.__changes.append([square, position[0], position[1]])

    def add_piece(self, canvas, x, y):
        piece = self.__table.get_piece(x, y)
        self.__pieces_dict[(x,y)] = None
        if str(piece) != '.':
            piece = canvas.create_oval((x-1)*80 + 20, (9-y-1)*80 + 20, x*80-20, (9-y)*80-20)
            self.__pieces_dict[(x,y)] = piece
            if y in (7,8):
                canvas.itemconfig(piece, fill = 'black')
            elif y in (1,2):
                canvas.itemconfig(piece, fill = 'white')

    def undo_click(self):
        for element in self.__changes:
            square = element[0]
            x = element[1]
            y = element[2]
            if (x + y) % 2 == 0:
                self.__canvas.itemconfig(square, fill=self.__colors['board1'])
            else:
                self.__canvas.itemconfig(square, fill=self.__colors['board2'])

    # def move(self, event):
    #     x, y = event.x, event.y
    #     piece = self.
    #     print('{}, {}'.format(x, y))
    #     self.__canvas.move(piece, x - x_img, y - y_img)
    #     x_img = x
    #     y_img = y
    #     canvas.update()


table = ChessTable()
root = Tk()
interface = GUI(table, root)
interface.convert_board_to_interface()
root.mainloop()

