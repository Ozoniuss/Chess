from tkinter import *
from chessTable import ChessTable
from PIL import ImageTk, Image


class GUI:
    def __init__(self, table, master):
        self.__table = table
        self.__frame = Frame(master,  width=2000, height=2000, bg = 'gray20')
        root.state('zoomed')
        self.__frame.grid(row=0, column=0, sticky='nesw')
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        self.__colors = {'board1' : 'MistyRose3',
                         'board2' : 'steel blue',
                         'when clicked2': 'SteelBlue2',
                         'when clicked1': 'MistyRose2',
                         'available position': 'AntiqueWhite1',
                         'frame' : 'gray20',
                         'button leave': 'gray27',
                         'button enter': 'gray36'
                        }
        self.__square_dict = {} # 0: square, 1: image, 2: color
        self.__changes = []
        # used for move function
        self.__piece_x = None
        self.__piece_y = None
        self.__piece_drawing = None
        self.__piece_coordinates = None
        self.__current_player = 'white'
        self.__previous_click = None

    def run_game(self):
        for widget in self.__frame.winfo_children():
            widget.destroy()

        self.__table = ChessTable()
        welcome_label = Label(self.__frame, text='\nWelcome to \n CHESS!\n', font=('MS Serif',50),
                              fg=self.__colors['available position'], bg=self.__colors['frame'])
        welcome_label.grid(row=1, rowspan = 4, column=2, sticky = 'sw')

        button_player = Button(self.__frame, text='Another player', height=4, width=30,
                               command=lambda: self.convert_board_to_interface(), bg=self.__colors['button leave'],
                               activebackground=self.__colors['button enter'], fg='white', font = ('MS Serif', 15))
        button_player.grid(row=5, column=2, pady = (0,0), sticky = 'sw')
        button_player.bind("<Enter>", lambda event, button = button_player: self.on_enter(button))
        button_player.bind("<Leave>", lambda event, button = button_player: self.on_leave(button))

        button_computer = Button(self.__frame, text='Computer', height=4, width=30,
                               command=lambda: self.computer, bg=self.__colors['button leave'],
                               activebackground=self.__colors['button enter'], fg='white', font = ('MS Serif', 15))
        button_computer.grid(row=6, column=2, pady = (0,0), sticky = 'sw')
        button_computer.bind("<Enter>", lambda event, button = button_computer: self.on_enter(button))
        button_computer.bind("<Leave>", lambda event, button = button_computer: self.on_leave(button))

        canvas = self.draw_board()
        canvas.grid(row=1, rowspan=6, column=1, padx=50, pady=(50,0), sticky=S)

    def on_enter(self, button):
        button['background'] = self.__colors['button enter']

    def on_leave(self, button):
        button['background'] = self.__colors['button leave']

    def computer(self):
        pass

    def convert_board_to_interface(self):
        for widget in self.__frame.winfo_children():
            widget.destroy()

        self.__table = ChessTable()
        self.__square_dict = {}
        self.__piece_drawing = None
        self.__changes = []
        self.__current_player = 'white'

        self.__canvas = self.draw_board()
        self.__canvas.grid(row=1, column=1, padx=50, pady=50, sticky=S)

        self.__canvas.bind('<Button-1>', self.click_handler)
        self.__canvas.bind('<B1-Motion>', self.move)
        self.__canvas.bind('<ButtonRelease-1>', self.check_position)
        self.__canvas.bind('<Motion>', self.motion)

        button1 = Button(self.__frame, text='New game', height=1, width=7, command=self.run_game,
                               bg=self.__colors['button leave'], activebackground=self.__colors['button enter'],
                               fg='white', font = ('MS Serif', 12))
        button1.grid(row=1, column=2, padx = 20, pady=50, ipadx=60, ipady=12, sticky=S)
        button1.bind("<Enter>", lambda event, button = button1: self.on_enter(button))
        button1.bind("<Leave>", lambda event, button = button1: self.on_leave(button))

        button2 = Button(self.__frame, text='Reset', height=1, width=7, command=self.convert_board_to_interface,
                               bg=self.__colors['button leave'], activebackground=self.__colors['button enter'],
                               fg='white', font = ('MS Serif', 12))
        button2.grid(row=1, column=3, padx = 20, pady=50, ipadx=60, ipady=12, sticky=S)
        button2.bind("<Enter>", lambda event, button = button2: self.on_enter(button))
        button2.bind("<Leave>", lambda event, button = button2: self.on_leave(button))

        button3 = Button(self.__frame, text='Exit', height=1, width=7, command=self.__frame.quit,
                               bg=self.__colors['button leave'], activebackground=self.__colors['button enter'],
                               fg='white', font = ('MS Serif', 12))
        button3.grid(row=1, column=4, padx=20, pady=50, ipadx=60, ipady=12, sticky=S)
        button3.bind("<Enter>", lambda event, button = button3: self.on_enter(button))
        button3.bind("<Leave>", lambda event, button = button3: self.on_leave(button))

    def draw_board(self):
        canvas = Canvas(self.__frame, width=641, height=641, highlightthickness=0, bg=self.__colors['board2'])
        self.__table.populate_chess_table()
        print(str(self.__table))
        for x in range(1, 9):
            for y in range(8, 0, -1):
                square = canvas.create_rectangle((x - 1) * 80, (9 - y - 1) * 80, x * 80, (9 - y) * 80)
                self.__square_dict[(x, y)] = [square, None, None]
                if (x + y) % 2 == 0:
                    canvas.itemconfig(square, fill=self.__colors['board1'])
                else:
                    canvas.itemconfig(square, fill=self.__colors['board2'])
                self.add_piece(canvas, x, y)
                if x == 1:
                    canvas.create_text((x - 1) * 80 + 10, (9 - y - 1) * 80 + 10, text=str(y))
                if y == 1:
                    canvas.create_text(x * 80 - 10, (9 - y) * 80 - 10, text=chr(ord('A') + x - 1))
        return canvas

    def add_piece(self, canvas, x, y):
        piece = self.__table.get_piece(x, y)
        color = piece.get_piece_info()[0]
        type = piece.get_piece_info()[1]
        piece_drawing = None
        self.__square_dict[(x, y)][2] = color
        if color == 'white':
            if type == 'pawn':
                img = Image.open('white_pawn.png')
                if x == 1:
                    canvas.img1 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img1)
                elif x == 2:
                    canvas.img2 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img2)
                elif x == 3:
                    canvas.img3 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img3)
                elif x == 4:
                    canvas.img4 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img4)
                elif x == 5:
                    canvas.img5 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img5)
                elif x == 6:
                    canvas.img6 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img6)
                elif x == 7:
                    canvas.img7 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img7)
                else:
                    canvas.img8 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img8)
            elif type == 'rock':
                img = Image.open('white_rock.png')
                if x == 1:
                    canvas.img9 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img9)
                elif x == 8:
                    canvas.img10 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img10)
            elif type == 'knight':
                img = Image.open('white_knight.png')
                if x == 2:
                    canvas.img11 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img11)
                elif x == 7:
                    canvas.img12 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img12)
            elif type == 'bishop':
                img = Image.open('white_bishop.png')
                if x == 3:
                    canvas.img13 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img13)
                elif x == 6:
                    canvas.img14 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img14)
            elif type == 'queen':
                img = Image.open('white_queen.png')
                canvas.img15 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                           image=canvas.img15)
            elif type == 'king':
                img = Image.open('white_king.png')
                canvas.img16 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                           image=canvas.img16)

        else:
            if type == 'pawn':
                img = Image.open('black_pawn.png')
                if x == 1:
                    canvas.img17 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img17)
                elif x == 2:
                    canvas.img18 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img18)
                elif x == 3:
                    canvas.img19 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img19)
                elif x == 4:
                    canvas.img20 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img20)
                elif x == 5:
                    canvas.img21 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img21)
                elif x == 6:
                    canvas.img22 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img22)
                elif x == 7:
                    canvas.img23 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img23)
                else:
                    canvas.img24 = ImageTk.PhotoImage(img.resize((40,50), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img24)
            elif type == 'rock':
                img = Image.open('black_rock.png')
                if x == 1:
                    canvas.img25 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img25)
                elif x == 8:
                    canvas.img26 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img26)
            elif type == 'knight':
                img = Image.open('black_knight.png')
                if x == 2:
                    canvas.img27 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img27)
                elif x == 7:
                    canvas.img28 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img28)
            elif type == 'bishop':
                img = Image.open('black_bishop.png')
                if x == 3:
                    canvas.img29 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img29)
                elif x == 6:
                    canvas.img30 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                    piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                               image=canvas.img30)
            elif type == 'queen':
                img = Image.open('black_queen.png')
                canvas.img31 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                           image=canvas.img31)
            elif type == 'king':
                img = Image.open('black_king.png')
                canvas.img32 = ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS))
                piece_drawing = canvas.create_image((x - 1) * 80 + 40, (8 - y) * 80 + 40,
                                                           image=canvas.img32)
        # self.__canvas.lift(piece_drawing)
        self.__square_dict[(x, y)][1] = piece_drawing

    def undo_click(self):
        for element in self.__changes:
            square = element[0]
            x = element[1]
            y = element[2]
            if (x + y) % 2 == 0:
                self.__canvas.itemconfig(square, fill=self.__colors['board1'])
            else:
                self.__canvas.itemconfig(square, fill=self.__colors['board2'])

    def click_handler(self, event):
        x = event.x // 80 + 1
        y = 8 - event.y // 80
        if x not in range(1, 9) or y not in range(1, 9): # we are not on the board
            self.__piece_drawing = None
            return
        if self.__square_dict[(x,y)][1] is None and self.__canvas.itemcget(self.__square_dict[(x,y)][0], 'fill') != self.__colors['available position']:
            # empty, not available square
            self.__piece_drawing = None
            return
        if self.__canvas.itemcget(self.__square_dict[(x,y)][0], 'fill') == self.__colors['available position']:
            pass # check_position will do the work
        else:
            # we are on a square with a piece in it
            # we color it
            self.__piece_x = event.x
            self.__piece_y = event.y
            self.__piece_drawing = self.__square_dict[(x, y)][1]
            self.undo_click()
            square = self.__square_dict[(x,y)][0]
            if self.__canvas.itemcget(self.__square_dict[(x,y)][0], 'fill') == self.__colors['board1']:
                self.__canvas.itemconfig(square, fill = self.__colors['when clicked1'])
            else:
                self.__canvas.itemconfig(square, fill=self.__colors['when clicked2'])
            self.__changes.append([square, x, y])
            piece = self.__table.get_piece(x, y)
            self.__piece_coordinates = [x,y]
            if self.__square_dict[(x,y)][2] == self.__current_player:
                # we show available positions only if it's our turn
                available_positions = piece.get_available_moves(self.__table, x, y)
                for position in available_positions:
                    square = self.__square_dict[(position[0], position[1])][0]
                    self.__canvas.itemconfig(square, fill=self.__colors['available position'])
                    self.__changes.append([square, position[0], position[1]])

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
        threatened_piece_drawing = self.__square_dict[(x,y)][1]
        square_color = self.__canvas.itemcget(square, 'fill')
        piece_color = self.__square_dict[(self.__piece_coordinates[0], self.__piece_coordinates[1])][2]
        if square_color == self.__colors['available position']: # a move has been made
            self.__table.move_piece(self.__piece_coordinates[0], self.__piece_coordinates[1], x, y)
            self.__square_dict[(x,y)][1] = self.__piece_drawing
            self.__square_dict[(x, y)][2] = piece_color
            self.change_player()
            self.undo_click()
            self.__canvas.coords(self.__piece_drawing, (x - 1) * 80 + 40, (9 - y - 1) * 80 + 40)
            # self.slide(self.__piece_drawing, self.__piece_x, self.__piece_y, (x-1)*80, (8-y)*80)
            self.__piece_drawing = None
            # self.__square_dict[(self.__piece_coordinates[0], self.__piece_coordinates[1])][1] = None
            del self.__square_dict[(self.__piece_coordinates[0], self.__piece_coordinates[1])]
            self.__canvas.delete(threatened_piece_drawing)
        else:
            x = self.__piece_coordinates[0]
            y = self.__piece_coordinates[1]
            self.__canvas.coords(self.__piece_drawing, (x - 1) * 80 + 40, (9 - y - 1) * 80 + 40)

    def motion(self, event):
        x = event.x // 80 + 1
        y = 8 - event.y // 80
        if x not in range(1, 9) or y not in range(1, 9): # we are not on the board
            self.__canvas.config(cursor="")
        elif self.__square_dict[(x,y)][1] is None:
            self.__canvas.config(cursor="")
        else:
            self.__canvas.config(cursor="hand1")

    # def slide(self, piece, initial_x, initial_y, final_x, final_y):
    #     x_rate = (final_x-initial_x)//100
    #     y_rate = (final_y-initial_y)//100
    #     while initial_x != final_x and initial_y != final_y:
    #         self.__canvas.move(piece, x_rate, y_rate)
    #         root.after(25, self.slide)
    #         initial_x += x_rate
    #         initial_y += y_rate

    def change_player(self):
        if self.__current_player == 'white':
            self.__current_player = 'black'
        else:
            self.__current_player = 'white'


table = ChessTable()
root = Tk()
interface = GUI(table, root)
interface.run_game()
root.mainloop()

