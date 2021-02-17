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
        self.__canvas = Canvas(self.__frame, width=700, height=700, highlightthickness=0)
        self.__changes = []
        # used for move function
        self.__piece_x = None
        self.__piece_y = None
        self.__piece_drawing = None
        self.__piece_coordinates = None

    def convert_board_to_interface(self):
        self.__table.populate_chess_table()
        for x in range(1,9):
            for y in range(8,0,-1):
                square = self.__canvas.create_rectangle((x-1)*80, (9-y-1)*80, x*80, (9-y)*80)
                self.__square_dict[(x,y)] = [square, None]
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
        self.__canvas.bind('<B1-Motion>', self.move)
        self.__canvas.bind('<ButtonRelease-1>', self.check_position)

    def click_handler(self, event):
        x = event.x//80 + 1
        y = 8 - event.y//80
        self.__piece_x = event.x
        self.__piece_y = event.y
        self.__piece_drawing = self.__square_dict[(x, y)][1]
        if x not in range(1,9) or y not in range(1,9):
            pass
        else:
            self.undo_click()
            square = self.__square_dict[(x,y)][0]
            self.__canvas.itemconfig(square, fill = self.__colors['when clicked'])
            self.__changes.append([square, x, y])
            piece = self.__table.get_piece(x, y)
            self.__piece_coordinates = [x,y]
            available_positions = piece.get_available_moves(self.__table, x, y)
            for position in available_positions:
                square = self.__square_dict[(position[0], position[1])][0]
                self.__canvas.itemconfig(square, fill=self.__colors['available position'])
                self.__changes.append([square, position[0], position[1]])

    def add_piece(self, canvas, x, y):
        piece = self.__table.get_piece(x, y)
        if str(piece) != '.':
            piece_drawing = canvas.create_oval((x-1)*80 + 20, (9-y-1)*80 + 20, x*80-20, (9-y)*80-20)
            self.__square_dict[(x,y)][1] = piece_drawing
            canvas.itemconfig(piece_drawing, fill = piece.get_piece_info()[0])

    def undo_click(self):
        for element in self.__changes:
            square = element[0]
            x = element[1]
            y = element[2]
            if (x + y) % 2 == 0:
                self.__canvas.itemconfig(square, fill=self.__colors['board1'])
            else:
                self.__canvas.itemconfig(square, fill=self.__colors['board2'])

    def move(self, event):
        x, y = event.x, event.y
        if self.__piece_drawing is not None:
            self.__canvas.move(self.__piece_drawing, x - self.__piece_x, y - self.__piece_y)
            self.__piece_x = x
            self.__piece_y = y
            self.__canvas.lift(self.__piece_drawing)
            self.__canvas.update()

    def check_position(self, event):
        x = event.x // 80 + 1
        y = 8 - event.y // 80
        square = self.__square_dict[(x,y)][0]
        # piece_drawing = self.__square_dict[(x,y)][1]
        color = self.__canvas.itemcget(square, 'fill')
        if color == self.__colors['available position']:
            self.__table.move_piece(self.__piece_coordinates[0], self.__piece_coordinates[1], x, y)
            self.__square_dict[(x,y)][1] = self.__piece_drawing
            print(str(self.__table))
        else:
            x = self.__piece_coordinates[0]
            y = self.__piece_coordinates[1]
        self.__canvas.coords(self.__piece_drawing, (x - 1) * 80 + 20, (9 - y - 1) * 80 + 20, x * 80 - 20, (9 - y) * 80 - 20)


table = ChessTable()
root = Tk()
interface = GUI(table, root)
interface.convert_board_to_interface()
root.mainloop()