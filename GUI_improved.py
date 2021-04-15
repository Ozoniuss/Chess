from tkinter import *
from chessTable import ChessTable
from PIL import ImageTk, Image
from functools import partial
from tkinter import ttk
from tkinter import  colorchooser


class Square:
    def __init__(self, square, photo_image, colour):
        self.__square = square
        self.__photo_image = photo_image
        self.__colour = colour

    def get_square(self):
        return self.__square

    def get_photo_image(self):
        return self.__photo_image

    def get_colour(self):
        return self.__colour

    def set_square(self, square):
        self.__square = square

    def set_photo_image(self, image):
        self.__photo_image = image

    def set_colour(self, colour):
        self.__colour = colour

    def reset(self):
        self.__photo_image = None
        self.__colour = None


class GUI:
    def __init__(self, table, master):
        self.__table = table
        self.__frame = Frame(master,  width=2000, height=2000, bg = 'gray20')
        root.state('zoomed')
        self.__frame.grid(row=0, column=0, sticky='nesw')
        self.__frame.grid_propagate(False)
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        self.__colors = {'board1' : '#dcbfb4',
                         'board2' : 'steel blue',
                         'when clicked2': 'SteelBlue2',
                         'when clicked1': 'MistyRose2',
                         'available position': 'AntiqueWhite1',
                         'frame' : 'gray20',
                         'button leave': 'gray27',
                         'button enter': 'gray36',
                         'text': 'white',
                         'status': 'gray36'
                        }
        self.__images = {('pawn', 'black') : 'black_pawn.png',
                         ('pawn', 'white'): 'white_pawn.png',
                         ('bishop', 'black'): 'black_bishop.png',
                         ('bishop', 'white'): 'white_bishop.png',
                         ('knight', 'black'): 'black_knight.png',
                         ('knight', 'white'): 'white_knight.png',
                         ('rock', 'black'): 'black_rock.png',
                         ('rock', 'white'): 'white_rock.png',
                         ('king', 'black'): 'black_king.png',
                         ('king', 'white'): 'white_king.png',
                         ('queen', 'black'): 'black_queen.png',
                         ('queen', 'white'): 'white_queen.png'
                         }

        self.__status_bar_black ={'pawn' : [],
                                  'bishop': [],
                                  'knight': [],
                                  'rock': [],
                                  'queen': [],
                                  'king': []
                                }
        self.__status_bar_white ={'pawn' : [],
                                  'bishop': [],
                                  'knight': [],
                                  'rock': [],
                                  'queen': [],
                                  'king': []
                                }

        self.__square_size = 80
        self.__status_size = 20
        self.__status_size_overlap = 7
        self.__canvas_white = None
        self.__canvas_black = None
        self.__white_score = 0
        self.__black_score = 0
        self.__white_pixels = 100
        self.__black_pixels = 100

        # dict keys: tuples of form (x,y), where x and y are the positions on the board
        # dict values: objects of class Square
        self.__square_dict = {}
        self.__changes = []
        # used for move function
        self.__piece_x = None
        self.__piece_y = None
        # the current piece we are working with
        self.__piece_drawing = None
        self.__piece_coordinates = None
        self.__current_player = 'white'
        self.__previous_click = None
        self.__canvas = None
        self.__photo_references = []

        self.__board_orientation = "wd"  # white down

        self.__dark_mode = "On"

    def reset(self):
        self.__table = ChessTable()
        self.__square_dict = {}
        self.__piece_drawing = None
        self.__changes = []
        self.__current_player = 'white'

        for type in self.__status_bar_black:
            self.__status_bar_black[type] = []
            self.__status_bar_white[type] = []

        self.__canvas_white = None
        self.__canvas_black = None
        self.__white_score = 0
        self.__black_score = 0
        self.__white_pixels = 100
        self.__black_pixels = 100

    def run_game(self):
        for widget in self.__frame.winfo_children():
            widget.destroy()

        self.reset()
        self.__table = ChessTable()
        welcome_label = Label(self.__frame, text='\nWelcome to \nCHESS!\n', font=('MS Serif', 50),
                              fg=self.__colors['text'], bg=self.__colors['frame'])
        welcome_label.grid(row=2, rowspan=4, column=2, sticky='sw')

        button_player = Button(self.__frame, text='Another player', height=4, width=30,
                               command=lambda: self.player(), bg=self.__colors['button leave'],
                               activebackground=self.__colors['button enter'], fg=self.__colors['text'], font=('MS Serif', 15))
        button_player.grid(row=7, column=2, pady=(0, 0), sticky='sw')
        button_player.bind("<Enter>", lambda event, button=button_player: self.on_enter(button))
        button_player.bind("<Leave>", lambda event, button=button_player: self.on_leave(button))

        button_computer = Button(self.__frame, text='Computer', height=4, width=30,
                                 command=lambda: self.computer(), bg=self.__colors['button leave'],
                                 activebackground=self.__colors['button enter'], fg=self.__colors['text'], font=('MS Serif', 15))
        button_computer.grid(row=8, column=2, pady=(0, 0), sticky='sw')
        button_computer.bind("<Enter>", lambda event, button=button_computer: self.on_enter(button))
        button_computer.bind("<Leave>", lambda event, button=button_computer: self.on_leave(button))

        self.__table.populate_chess_table()
        self.draw_board()
        self.__canvas.grid(row=1, rowspan=8, column=1, padx=50, pady=(70, 0), sticky=S)

    def player(self):
        self.convert_board_to_interface()
        self.create_status_bars()

    def computer(self):
        pass

    def on_enter(self, button):
        button['background'] = self.__colors['button enter']

    def on_leave(self, button):
        button['background'] = self.__colors['button leave']

    def on_leave_standard(self, button):
        button['background'] = self.__colors['frame']

    def draw_board(self):
        canvas = Canvas(self.__frame, width=641, height=641, highlightthickness=0, bg=self.__colors['board2'])
        self.__canvas = canvas

        for x in range(1, 9):
            for y in range(8, 0, -1):

                cnv_x, cnv_y = self.choose_coordinates(x, y)

                square = canvas.create_rectangle((cnv_x - 1) * self.__square_size, (9 - cnv_y - 1) * self.__square_size, cnv_x * self.__square_size, (9 - cnv_y) * self.__square_size)

                self.__square_dict[(x, y)] = Square(square, None, None)
                if (x + y) % 2 == 0:
                    canvas.itemconfig(square, fill=self.__colors['board1'])
                else:
                    canvas.itemconfig(square, fill=self.__colors['board2'])
                self.add_piece( x, y)

                cnv_x, cnv_y = self.choose_coordinates(x, y)
                self.add_text_to_board(cnv_x, cnv_y)

    def add_text_to_board(self, cnv_x, cnv_y):
        if cnv_x == 1:
            if self.__board_orientation == 'wd':
                self.__canvas.create_text((cnv_x - 1) * self.__square_size + 10, (9 - cnv_y - 1) * self.__square_size + 10,
                                   text=str(cnv_y))
            else:
                self.__canvas.create_text((cnv_x - 1) * self.__square_size + 10, (9 - cnv_y - 1) * self.__square_size + 10,
                                   text=str(9 - cnv_y))
        if cnv_y == 1:
            if self.__board_orientation == 'wd':
                self.__canvas.create_text(cnv_x * self.__square_size - 10, (9 - cnv_y) * self.__square_size - 10,
                                   text=chr(ord('A') + cnv_x - 1))
            else:
                self.__canvas.create_text(cnv_x * self.__square_size - 10, (9 - cnv_y) * self.__square_size - 10,
                                   text=chr(ord('A') + 9 - cnv_x - 1))

    def add_piece(self, x, y):
        piece = self.__table.get_piece(x, y)
        color = piece.get_piece_color_and_type()[0]
        type = piece.get_piece_color_and_type()[1]
        self.__square_dict[(x, y)].set_colour(color)
        if color is not None and type is not None:
            img = Image.open(self.__images[(type, color)])
            if type == 'pawn':
                self.__photo_references.append(ImageTk.PhotoImage(img.resize((40, 50), Image.ANTIALIAS)))
            else:
                self.__photo_references.append(ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS)))

            cnv_x, cnv_y = self.choose_coordinates(x, y)
            piece_drawing = self.__canvas.create_image((cnv_x - 1) * self.__square_size + self.__square_size / 2,
                                                (8 - cnv_y) * self.__square_size + self.__square_size / 2,
                                                image=self.__photo_references[len(self.__photo_references)-1])

            self.__square_dict[(x, y)].set_photo_image(piece_drawing)

    def create_status_bars(self):
        self.__canvas_black = Canvas(self.__frame, width=641, height=40, highlightthickness=0, bg=self.__colors['status'])
        self.__canvas_black.create_text(55, 20, text="Black player", fill="Black",font=('MS Serif', 12))
        self.__canvas_white = Canvas(self.__frame, width=641, height=40, highlightthickness=0, bg=self.__colors['status'])
        self.__canvas_white.create_text(55, 20, text="White player", fill="White", font=('MS Serif', 13))
        if self.__board_orientation == 'wd':
            self.__canvas_black.grid(row=1, column=1, padx=(50, 0), pady=10, sticky=S)
            self.__canvas_white.grid(row=34, column=1, padx=(50, 0), pady=10, sticky=S)
        else:
            self.__canvas_black.grid(row=34, column=1, padx=(50, 0), pady=10, sticky=S)
            self.__canvas_white.grid(row=1, column=1, padx=(50, 0), pady=10, sticky=S)

    def create_canvas(self):
        self.draw_board()
        self.__canvas.grid(row=2, column=1, rowspan = 32, padx=(50, 0), pady=10, sticky=S)

        self.__canvas.bind('<Button-1>', self.click_handler)
        self.__canvas.bind('<B1-Motion>', self.move)
        self.__canvas.bind('<ButtonRelease-1>', self.unclick_handler)
        self.__canvas.bind('<Motion>', self.motion)

    def convert_board_to_interface(self):
        for widget in self.__frame.winfo_children():
            widget.destroy()

        self.create_canvas()

        button1 = Button(self.__frame, text='New game', height=1, width=7, command=self.run_game,
                               bg=self.__colors['button leave'], activebackground=self.__colors['button enter'],
                               fg=self.__colors['text'], font = ('MS Serif', 12))
        button1.grid(row=33, column=3, padx = 20, pady=(0,10), ipadx=60, ipady=12, sticky=S)
        button1.bind("<Enter>", lambda event, button = button1: self.on_enter(button))
        button1.bind("<Leave>", lambda event, button = button1: self.on_leave(button))

        button2 = Button(self.__frame, text='Reset', height=1, width=7, command=self.in_game_reset,
                               bg=self.__colors['button leave'], activebackground=self.__colors['button enter'],
                               fg=self.__colors['text'], font = ('MS Serif', 12))
        button2.grid(row=33, column=4, padx = 20, pady=(0,10), ipadx=60, ipady=12, sticky=S)
        button2.bind("<Enter>", lambda event, button = button2: self.on_enter(button))
        button2.bind("<Leave>", lambda event, button = button2: self.on_leave(button))

        button3 = Button(self.__frame, text='Exit', height=1, width=7, command=self.__frame.quit,
                               bg=self.__colors['button leave'], activebackground=self.__colors['button enter'],
                               fg=self.__colors['text'], font = ('MS Serif', 12))
        button3.grid(row=33, column=5, padx=20, pady=(0,10), ipadx=60, ipady=12, sticky=S)
        button3.bind("<Enter>", lambda event, button = button3: self.on_enter(button))
        button3.bind("<Leave>", lambda event, button = button3: self.on_leave(button))

        img = Image.open("refresh.png")
        self.__photo_references.append(ImageTk.PhotoImage(img.resize((15, 15), Image.ANTIALIAS)))

        button4 = Button(self.__frame, image = self.__photo_references[len(self.__photo_references)-1], height=20, width=20, command=self.reverse_board,
                               bg=self.__colors['frame'], activebackground=self.__colors['button enter'],
                               fg=self.__colors['text'], font = ('MS Serif', 12), borderwidth=0)
        button4.grid(row=2, column=2, padx=10, pady=(11, 0), sticky=NW)
        button4.bind("<Enter>", lambda event, button = button4: self.on_leave(button))
        button4.bind("<Leave>", lambda event, button = button4: self.on_leave_standard(button))

        img = Image.open("settings.png")
        self.__photo_references.append(ImageTk.PhotoImage(img.resize((15, 15), Image.ANTIALIAS)))

        button5 = Button(self.__frame, image = self.__photo_references[len(self.__photo_references)-1], height=20, width=20, command=self.popupmsg,
                         bg=self.__colors['frame'], activebackground=self.__colors['button enter'],
                         fg=self.__colors['text'], font = ('MS Serif', 12), borderwidth=0)
        button5.grid(row=3, column=2, padx=10, pady=0, sticky=NW)
        button5.bind("<Enter>", lambda event, button = button5: self.on_leave(button))
        button5.bind("<Leave>", lambda event, button = button5: self.on_leave_standard(button))

    def in_game_reset(self):
        self.reset()
        self.__table.populate_chess_table()
        self.convert_board_to_interface()
        self.create_status_bars()

    def undo_click(self):
        # when we press on a square, we want to uncolour the available positions we had before
        for element in self.__changes:
            square = element[0]
            x = element[1]
            y = element[2]
            if (x + y) % 2 == 0:
                self.__canvas.itemconfig(square, fill=self.__colors['board1'])
            else:
                self.__canvas.itemconfig(square, fill=self.__colors['board2'])
        self.__changes.clear()

    def click_handler(self, event):
        x = event.x // 80 + 1
        y = 8 - event.y // 80

        x, y = self.choose_coordinates(x, y)

        if x not in range(1, 9) or y not in range(1, 9): # we are not on the board
            self.__piece_drawing = None
            return
        if self.__square_dict[(x,y)].get_photo_image() is None and self.__canvas.itemcget(self.__square_dict[(x, y)].get_square(), 'fill') != self.__colors['available position']:
            # empty, not available square
            self.__piece_drawing = None
            return
        if self.__canvas.itemcget(self.__square_dict[(x, y)].get_square(), 'fill') == self.__colors['available position']:
            # we press an available square <=> we want to actually make the move
            pass # unclick_handler will do the work
        else:
            # we are on a square with a piece in it
            # we color it
            self.__piece_x = event.x
            self.__piece_y = event.y
            self.__piece_drawing = self.__square_dict[(x, y)].get_photo_image()
            self.undo_click()
            square = self.__square_dict[(x, y)].get_square()
            # coloring the pressed square
            if self.__canvas.itemcget(self.__square_dict[(x, y)].get_square(), 'fill') == self.__colors['board1']:
                self.__canvas.itemconfig(square, fill = self.__colors['when clicked1'])
            else:
                self.__canvas.itemconfig(square, fill=self.__colors['when clicked2'])
            self.__changes.append([square, x, y])
            piece = self.__table.get_piece(x, y)
            self.__piece_coordinates = [x, y]
            if self.__square_dict[(x, y)].get_colour() == self.__current_player:
                # we show available positions only if it's our turn
                available_positions = piece.get_available_moves(self.__table, x, y)
                for position in available_positions:
                    square = self.__square_dict[(position[0], position[1])].get_square()
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

    def unclick_handler(self, event):
        x = event.x // 80 + 1
        y = 8 - event.y // 80

        x, y = self.choose_coordinates(x, y)

        if (x < 1 or x > 8) or (y < 1 or y > 8): # not on the board
            self.return_piece_to_its_place()
            return
        square = self.__square_dict[(x,y)].get_square()
        square_color = self.__canvas.itemcget(square, 'fill')
        piece_color = self.__square_dict[(self.__piece_coordinates[0], self.__piece_coordinates[1])].get_colour()
        if self.__piece_drawing is not None: # we only do something if a piece was selected
            if square_color == self.__colors['available position']: # a move has been made
                self.undo_click()

                # check if a piece was taken out and if so, add it to the status bar
                self.get_piece_out(x, y)

                self.__table.move_piece(self.__piece_coordinates[0], self.__piece_coordinates[1], x, y)
                self.change_player()

                self.create_canvas()

                self.__piece_drawing = None
                self.__square_dict[(self.__piece_coordinates[0], self.__piece_coordinates[1])].reset()
            else:
                # return the piece to its original position
                self.return_piece_to_its_place()

    def return_piece_to_its_place(self):
        x = self.__piece_coordinates[0]
        y = self.__piece_coordinates[1]
        cnv_x, cnv_y = self.choose_coordinates(x, y)
        self.__canvas.coords(self.__piece_drawing, (cnv_x - 1) * 80 + 40, (9 - cnv_y - 1) * 80 + 40)

    def change_player(self):
        if self.__current_player == 'white':
            self.__current_player = 'black'
        else:
            self.__current_player = 'white'

    def motion(self, event):
        x = event.x // 80 + 1
        y = 8 - event.y // 80

        if x not in range(1, 9) or y not in range(1, 9): # we are not on the board
            self.__canvas.config(cursor="")
        elif self.__square_dict[(x,y)].get_photo_image() is None:
            self.__canvas.config(cursor="")
        else:
            self.__canvas.config(cursor="hand1")

# Functions that handle the status bars #

    def get_greater_pieces(self, type):
        if type == 'pawn':
            return ['bishop', 'knight', 'rock', 'queen', 'king']
        elif type == 'bishop':
            return ['knight', 'rock', 'queen', 'king']
        elif type == 'knight':
            return ['rock', 'queen', 'king']
        elif type == 'rock':
            return ['queen', 'king']
        elif type == 'queen':
            return ['king']

    def switch_pieces_one_pos(self, color, type):
        # Because we want the pieces of the same kind to overlap, the amount of pixels
        # that the following pieces are moved depends if we have any pieces of "type" already out

        pieces_to_be_moved = self.get_greater_pieces(type)
        number_pieces_moved = 0
        pixels = self.__status_size
        if color == 'black':
            if len(self.__status_bar_white[type]) != 0:
                pixels = self.__status_size_overlap
            for piece_type in pieces_to_be_moved:
                for piece_drawing in self.__status_bar_white[piece_type]:
                    self.__canvas_white.move(piece_drawing, pixels, 0)
                    number_pieces_moved += 1
        elif color == 'white':
            if len(self.__status_bar_black[type]) != 0:
                pixels = self.__status_size_overlap
            for piece_type in pieces_to_be_moved:
                for piece_drawing in self.__status_bar_black[piece_type]:
                    self.__canvas_black.move(piece_drawing, pixels, 0)
                    number_pieces_moved += 1
        return number_pieces_moved, pixels

    def get_piece_out(self, x, y):
        threatened_piece_drawing = self.__square_dict[(x, y)].get_photo_image()
        if threatened_piece_drawing is not None:
            piece = self.__table.get_piece(x,y)
            color, type = piece.get_piece_color_and_type()
            # because we want to keep the pieces in order, we get a list of types of the pieces
            # that we move one position to the right
            number_pieces_moved, pixels = self.switch_pieces_one_pos(color, type)

            img = Image.open(self.__images[(type, color)])
            self.__photo_references.append(ImageTk.PhotoImage(img.resize((15, 20), Image.ANTIALIAS)))

            if self.__current_player == 'white': # we got out a black piece, which goes into the white dictionary
                image = self.__canvas_white.create_image((self.__white_pixels - self.__status_size * number_pieces_moved) + pixels, 20,
                                                image=self.__photo_references[len(self.__photo_references) - 1])
                self.__status_bar_white[type].append(image)
                self.__white_score += 1
                self.__white_pixels += pixels
            elif self.__current_player == 'black':
                image = self.__canvas_black.create_image((self.__black_pixels - self.__status_size * number_pieces_moved) + pixels, 20,
                                                image=self.__photo_references[len(self.__photo_references) - 1])
                self.__status_bar_black[type].append(image)
                self.__black_score += 1
                self.__black_pixels += pixels


# Functions that handle the reversing of the board #

    def choose_coordinates(self, x, y):
        a = x
        b = y
        if self.__board_orientation != 'wd':
            a = 9-x
            b = 9-y
        return a, b

    def reverse_board(self):
        self.undo_click()
        if self.__board_orientation == "wd":
            self.__board_orientation = "bd"
            self.__canvas_white.grid(row=1, column=1, padx=(50, 0), pady=10, sticky=S)
            self.__canvas_black.grid(row=34, column=1, padx=(50, 0), pady=10, sticky=S)
        else:
            self.__board_orientation = "wd"
            self.__canvas_white.grid(row=34, column=1, padx=(50, 0), pady=10, sticky=S)
            self.__canvas_black.grid(row=1, column=1, padx=(50, 0), pady=10, sticky=S)

        self.create_canvas()

# Functions that handle the settings #

    def dark_mode_colors(self):
        self.__colors['frame'] = 'gray20'
        self.__colors['button leave'] = 'gray27'
        self.__colors['button enter'] = 'gray36'
        self.__colors['text'] = 'white'
        self.__colors['status'] = 'gray36'

    def powder_mode_colors(self):
        self.__colors['frame'] = '#d7b19f'
        self.__colors['button leave'] = '#c9957c'
        self.__colors['button enter'] = '#d7b19f'
        self.__colors['text'] =  'black'
        self.__colors['status'] = '#c9957c'

    def set_board_color(self, variable):
        if variable == 'Blue':
            self.__colors['board2'] = 'steel blue'
            self.__colors['when clicked2'] = 'SteelBlue2'
        elif variable == "Green":
            self.__colors['board2'] = '#3a7e51'
            self.__colors['when clicked2'] = '#58c985'
        elif variable == "Violet":
            self.__colors['board2'] = "PaleVioletRed4"
            self.__colors['when clicked2'] = '#c18687'
        elif variable == "Red":
            self.__colors['board2'] = "indian red"
            self.__colors['when clicked2'] = '#ee9193'

    def set_dark_mode(self, state):
        if state == "Powder":
            self.powder_mode_colors()
        else:
            self.dark_mode_colors()
        self.__dark_mode = state

    def save_changes(self, root, *args):
        root.destroy()
        self.__frame.config(bg=self.__colors['frame'])
        self.convert_board_to_interface()
        self.create_status_bars()

    def create_combo(self, frame, options):
        combo = ttk.Combobox(frame, value=options)
        combo.current(0)
        combo['state'] = 'readonly'

        frame.option_add("*TCombobox*Listbox*Background", self.__colors['button leave'])
        frame.option_add('*TCombobox*Listbox.selectBackground', self.__colors['button enter'])  # change highlight color
        frame.option_add('*TCombobox*Listbox.selectForeground', self.__colors['text'])  # change text color

        return combo


    def popupmsg(self):
        new_root = Tk()
        new_root.title("Settings")
        new_root.resizable(False, False)
        frame = Frame(new_root,  width=300, height=500, bg = self.__colors['frame'])
        frame.grid(row=0, column=0)
        frame.grid_propagate(False)

        color_label = Label(frame, text="Board color:", bg=self.__colors['frame'], fg=self.__colors['text'])
        color_label.grid(row=0, column=0, padx=10, pady=10)

        dark_mode_label = Label(frame, text="Theme mode:", bg=self.__colors['frame'], fg=self.__colors['text'])
        dark_mode_label.grid(row=1, column=0, padx=10, pady=10)

        options = ["Blue", "Green", "Violet", "Red"]
        color_combo = self.create_combo(frame, options)
        color_combo.bind('<<ComboboxSelected>>', lambda event: self.set_board_color(color_combo.get()))
        color_combo.grid(row=0, column=1, padx=10, pady=10)

        options2 = ['Dark', 'Powder']
        dark_mode_combo = self.create_combo(frame, options2)
        dark_mode_combo.bind('<<ComboboxSelected>>', lambda event: self.set_dark_mode(dark_mode_combo.get()))
        dark_mode_combo.grid(row=1, column=1, padx=10, pady=10)

        B1 = Button(frame, text="Okay", height=2, width=10, command=partial(self.save_changes, new_root),
                    bg=self.__colors['button leave'], fg=self.__colors['text'])
        B1.grid(row=2,  padx=10, pady=20, sticky = 'ns')
        B1.bind("<Enter>", lambda event, button=B1: self.on_enter(button))
        B1.bind("<Leave>", lambda event, button=B1: self.on_leave(button))
        new_root.mainloop()

table = ChessTable()
root = Tk()
interface = GUI(table, root)
interface.run_game()
root.mainloop()