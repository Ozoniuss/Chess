from tkinter import *
from ChessTable.chessTable import ChessTable
from PIL import ImageTk, Image
from tkinter import ttk
from GUI.Square import Square
from GUI.PromotionTab import PromotionTab
from GUI.ImagesColors import ImagesColors
from Event.Events import *
from GUI.Status_bar import WhiteStatusBar, BlackStatusBar


class GUI:
    def __init__(self, table, master, client = False):
        self.__image_path = 'Pictures/'
        self.__root = master
        self.__table = table
        self.__frame = Frame(master,  width=2000, height=2000, bg = 'gray20')
        self.__root.state('zoomed')
        self.__frame.grid(row=0, column=0, sticky='nesw')
        self.__frame.grid_propagate(False)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)

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

        self.__images_colors = ImagesColors(self.__frame)
        self.__promotion_tab = PromotionTab(self.__root, self.__frame, self.__images_colors)

        self.client = client

        self.__white_status_bar = WhiteStatusBar(self.__frame, self.__images_colors)
        self.__black_status_bar = BlackStatusBar(self.__frame, self.__images_colors)

    @property
    def table(self):
        return self.__table

    def reset(self):
        self.__table = ChessTable()
        self.__square_dict = {}
        self.__piece_drawing = None
        self.__changes = []
        self.__current_player = 'white'

        for type in self.__status_bar_black:
            self.__status_bar_black[type] = []
            self.__status_bar_white[type] = []

        self.__white_status_bar = WhiteStatusBar(self.__frame, self.__images_colors)
        self.__black_status_bar = BlackStatusBar(self.__frame, self.__images_colors)

    def run_game(self):
        for widget in self.__frame.winfo_children():
            widget.destroy()

        self.reset()
        self.__table = ChessTable()
        welcome_label = Label(self.__frame, text='\nWelcome to \nCHESS!\n', font=('MS Serif', 50),
                              fg=self.__images_colors.get_color('text'), bg=self.__images_colors.get_color('frame'))
        welcome_label.grid(row=2, rowspan=4, column=2, sticky='sw')

        button_player = Button(self.__frame, text='Another player', height=4, width=30,
                               command=lambda: self.player(), bg=self.__images_colors.get_color('button leave'),
                               activebackground=self.__images_colors.get_color('button enter'), fg=self.__images_colors.get_color('text'), font=('MS Serif', 15))
        button_player.grid(row=7, column=2, pady=(0, 0), sticky='sw')
        button_player.bind("<Enter>", lambda event, button=button_player: self.on_enter(button))
        button_player.bind("<Leave>", lambda event, button=button_player: self.on_leave(button))

        button_computer = Button(self.__frame, text='Computer', height=4, width=30,
                                 command=lambda: self.computer(), bg=self.__images_colors.get_color('button leave'),
                                 activebackground=self.__images_colors.get_color('button enter'), fg=self.__images_colors.get_color('text'), font=('MS Serif', 15))
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
        button['background'] = self.__images_colors.get_color('button enter')

    def on_leave(self, button):
        button['background'] = self.__images_colors.get_color('button leave')

    def on_leave_standard(self, button):
        button['background'] = self.__images_colors.get_color('frame')

    def draw_board(self):
        canvas = Canvas(self.__frame, width=641, height=641, highlightthickness=0, bg=self.__images_colors.get_color('board2'))
        self.__canvas = canvas

        for x in range(1, 9):
            for y in range(8, 0, -1):

                cnv_x, cnv_y = self.choose_coordinates(x, y)

                square = canvas.create_rectangle((cnv_x - 1) * self.__square_size, (9 - cnv_y - 1) * self.__square_size, cnv_x * self.__square_size, (9 - cnv_y) * self.__square_size)

                self.__square_dict[(x, y)] = Square(square, None, None)
                if (x + y) % 2 == 0:
                    canvas.itemconfig(square, fill=self.__images_colors.get_color('board1'))
                else:
                    canvas.itemconfig(square, fill=self.__images_colors.get_color('board2'))
                self.add_piece(x,y)

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
            img = Image.open(self.__images_colors.get_image(type, color))

            self.__photo_references.append(ImageTk.PhotoImage(img.resize((self.__images_colors.image_width, self.__images_colors.image_height), Image.ANTIALIAS)))

            cnv_x, cnv_y = self.choose_coordinates(x, y)
            piece_drawing = self.__canvas.create_image((cnv_x - 1) * self.__square_size + self.__square_size / 2,
                                                (8 - cnv_y) * self.__square_size + self.__square_size / 2,
                                                image=self.__photo_references[len(self.__photo_references)-1])

            self.__square_dict[(x, y)].set_photo_image(piece_drawing)

    def create_status_bars(self):
        self.__white_status_bar.create_status_bar(self.__board_orientation)
        self.__black_status_bar.create_status_bar(self.__board_orientation)

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
                               bg=self.__images_colors.get_color('button leave'), activebackground=self.__images_colors.get_color('button enter'),
                               fg=self.__images_colors.get_color('text'), font = ('MS Serif', 12))
        button1.grid(row=33, column=3, padx = 20, pady=(0,10), ipadx=60, ipady=12, sticky=S)
        button1.bind("<Enter>", lambda event, button = button1: self.on_enter(button))
        button1.bind("<Leave>", lambda event, button = button1: self.on_leave(button))

        button2 = Button(self.__frame, text='Reset', height=1, width=7, command=self.in_game_reset,
                               bg=self.__images_colors.get_color('button leave'), activebackground=self.__images_colors.get_color('button enter'),
                               fg=self.__images_colors.get_color('text'), font = ('MS Serif', 12))
        button2.grid(row=33, column=4, padx = 20, pady=(0,10), ipadx=60, ipady=12, sticky=S)
        button2.bind("<Enter>", lambda event, button = button2: self.on_enter(button))
        button2.bind("<Leave>", lambda event, button = button2: self.on_leave(button))

        button3 = Button(self.__frame, text='Exit', height=1, width=7, command=self.__frame.quit,
                               bg=self.__images_colors.get_color('button leave'), activebackground=self.__images_colors.get_color('button enter'),
                               fg=self.__images_colors.get_color('text'), font = ('MS Serif', 12))
        button3.grid(row=33, column=5, padx=20, pady=(0,10), ipadx=60, ipady=12, sticky=S)
        button3.bind("<Enter>", lambda event, button = button3: self.on_enter(button))
        button3.bind("<Leave>", lambda event, button = button3: self.on_leave(button))

        img = Image.open(self.__image_path + "refresh.png")
        self.__photo_references.append(ImageTk.PhotoImage(img.resize((15, 15), Image.ANTIALIAS)))

        button4 = Button(self.__frame, image = self.__photo_references[len(self.__photo_references)-1], height=20, width=20, command=self.reverse_board,
                               bg=self.__images_colors.get_color('frame'), activebackground=self.__images_colors.get_color('button enter'),
                               fg=self.__images_colors.get_color('text'), font = ('MS Serif', 12), borderwidth=0)
        button4.grid(row=2, column=2, padx=10, pady=(11, 0), sticky=NW)
        button4.bind("<Enter>", lambda event, button = button4: self.on_leave(button))
        button4.bind("<Leave>", lambda event, button = button4: self.on_leave_standard(button))

        img = Image.open(self.__image_path + "settings.png")
        self.__photo_references.append(ImageTk.PhotoImage(img.resize((15, 15), Image.ANTIALIAS)))

        button5 = Button(self.__frame, image = self.__photo_references[len(self.__photo_references)-1], height=20, width=20, command=self.settings_tab,
                         bg=self.__images_colors.get_color('frame'), activebackground=self.__images_colors.get_color('button enter'),
                         fg=self.__images_colors.get_color('text'), font = ('MS Serif', 12), borderwidth=0)
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
                self.__canvas.itemconfig(square, fill=self.__images_colors.get_color('board1'))
            else:
                self.__canvas.itemconfig(square, fill=self.__images_colors.get_color('board2'))
        self.__changes.clear()

    def click_handler(self, event):
        x = event.x // 80 + 1
        y = 8 - event.y // 80

        x, y = self.choose_coordinates(x, y)

        if x not in range(1, 9) or y not in range(1, 9): # we are not on the board
            self.__piece_drawing = None
            return
        if self.__square_dict[(x,y)].get_photo_image() is None and self.__canvas.itemcget(self.__square_dict[(x, y)].get_square(), 'fill') != self.__images_colors.get_color('available position'):
            # empty, not available square
            return
        if self.__canvas.itemcget(self.__square_dict[(x, y)].get_square(), 'fill') == self.__images_colors.get_color('available position'):
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
            if self.__canvas.itemcget(self.__square_dict[(x, y)].get_square(), 'fill') ==self.__images_colors.get_color('board1'):
                self.__canvas.itemconfig(square, fill=self.__images_colors.get_color('when clicked1'))
            else:
                self.__canvas.itemconfig(square, fill=self.__images_colors.get_color('when clicked2'))
            self.__changes.append([square, x, y])
            piece = self.__table.get_piece(x, y)
            self.__piece_coordinates = [x, y]
            if self.__square_dict[(x, y)].get_colour() == self.__current_player:
                # we show available positions only if it's our turn
                available_positions = piece.get_available_moves(self.__table, x, y)
                for position in available_positions:
                    square = self.__square_dict[(position[0], position[1])].get_square()
                    self.__canvas.itemconfig(square, fill=self.__images_colors.get_color('available position'))
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
        if self.__piece_drawing is not None: # we only do something if a piece was selected
            if square_color == self.__images_colors.get_color('available position'): # a move has been made
                self.undo_click()

                # check if a piece was taken out and if so, add it to the status bar
                self.get_piece_out(x, y)

                promotion_piece = self.check_promotion( self.__piece_coordinates[0], self.__piece_coordinates[1], x, y)
                self.__promotion_tab.hide()

                # self.__table.move_piece(self.__piece_coordinates[0], self.__piece_coordinates[1], x, y, promotion_piece)
                post_event('GUI_moved', [self.__table, self.__piece_coordinates[0], self.__piece_coordinates[1], x, y, promotion_piece])
                if self.client:
                    post_event('Notify_server', [self.client, self.__table, self.__piece_coordinates[0], self.__piece_coordinates[1], x, y, promotion_piece])
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

# Promotion #

    def check_promotion(self, initial_x, initial_y, new_x, new_y):
        piece = self.__table.get_piece(initial_x, initial_y)
        selected_piece = None
        # pawn reaches the end and can promote
        if piece.get_piece_color_and_type() == ('white', 'pawn') and initial_y == 7 and new_y == 8:
            self.__promotion_tab.promotion_tab('white', self.__images_colors.get_color('frame'), self.__images_colors.get_color('frame'),
                                               self.__images_colors.get_color('button enter'), self.__images_colors.get_color('button leave'),
                                               self.__images_colors.get_color('frame'))

        # same for black pawn
        if piece.get_piece_color_and_type() == ('black', 'pawn') and initial_y == 2 and new_y == 1:
            self.__promotion_tab.promotion_tab('black', self.__images_colors.get_color('frame'), self.__images_colors.get_color('frame'),
                                               self.__images_colors.get_color('button enter'), self.__images_colors.get_color('button leave'),
                                               self.__images_colors.get_color('frame'))

        return self.__promotion_tab.get_promotion_piece()

# Functions that handle the status bars #

    def get_piece_out(self, x, y):
        threatened_piece_drawing = self.__square_dict[(x, y)].get_photo_image()
        if threatened_piece_drawing is not None:
            piece = self.__table.get_piece(x,y)
            color, type = piece.get_piece_color_and_type()

            if self.__current_player == 'black':
                self.__white_status_bar.get_piece_out(color, type)
            else:
                self.__black_status_bar.get_piece_out(color, type)

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
        else:
            self.__board_orientation = "wd"
        self.__white_status_bar.reverse(self.__board_orientation)
        self.__black_status_bar.reverse(self.__board_orientation)

        self.create_canvas()

# Functions that handle the settings #

    def set_board_color(self, variable):
        self.__images_colors.set_board_color(variable)
        self.create_canvas()

    def set_dark_mode(self, state):
        if state == "Powder":
            self.__images_colors.powder_mode_colors()
        else:
            self.__images_colors.dark_mode_colors()
        self.__dark_mode = state
        self.__frame.config(bg = self.__images_colors.get_color('frame'))
        self.convert_board_to_interface()
        self.create_status_bars()

    def change_pieces(self, variable):
        if variable == "Normal contour":
            self.__images_colors.set_pieces_normal()
        elif variable == "Drawing":
            self.__images_colors.set_pieces_drawing()
        elif variable == "Minimalist":
            self.__images_colors.set_pieces_minimalist()

        self.create_canvas()
        self.create_status_bars()

    def set_transparent(self, variable):
        if variable == "On":
            self.__images_colors.check_transparent()
        elif variable == "Off":
            self.__images_colors.check_full()

        self.create_canvas()
        self.create_status_bars()

    def create_combo(self, frame, options):
        combo = ttk.Combobox(frame, value=options)
        combo.set('...')
        combo['state'] = 'readonly'

        frame.option_add("*TCombobox*Listbox*Background", self.__images_colors.get_color('button leave'))
        frame.option_add('*TCombobox*Listbox.selectBackground', self.__images_colors.get_color('button enter'))  # change highlight color
        frame.option_add('*TCombobox*Listbox.selectForeground', self.__images_colors.get_color('text'))  # change text color

        return combo

    def settings_tab(self):
        new_root = Toplevel()
        new_root.title("Settings")
        new_root.resizable(False, False)
        frame = Frame(new_root,  width=300, height=500, bg = self.__images_colors.get_color('frame'))
        frame.grid(row=0, column=0)
        frame.grid_propagate(False)

        color_label = Label(frame, text="Board color:", bg=self.__images_colors.get_color('frame'), fg=self.__images_colors.get_color('text'))
        color_label.grid(row=0, column=0, padx=10, pady=10, sticky='E')

        theme_label = Label(frame, text="Theme mode:", bg=self.__images_colors.get_color('frame'), fg=self.__images_colors.get_color('text'))
        theme_label.grid(row=1, column=0, padx=10, pady=10, sticky='E')

        pieces_label = Label(frame, text="Pieces style:", bg=self.__images_colors.get_color('frame'), fg=self.__images_colors.get_color('text'))
        pieces_label.grid(row=2, column=0, padx=10, pady=10, sticky='E')

        transparency_label = Label(frame, text="Transparent piece:", bg=self.__images_colors.get_color('frame'), fg=self.__images_colors.get_color('text'))
        transparency_label.grid(row=3, column=0, padx=10, pady=10, sticky='E')

        options = ["Blue", "Green", "Violet", "Red"]
        color_combo = self.create_combo(frame, options)
        color_combo.bind('<<ComboboxSelected>>', lambda event: self.set_board_color(color_combo.get()))
        color_combo.grid(row=0, column=1, padx=10, pady=10)

        options2 = ['Dark', 'Powder']
        dark_mode_combo = self.create_combo(frame, options2)
        dark_mode_combo.bind('<<ComboboxSelected>>', lambda event: self.set_dark_mode(dark_mode_combo.get()))
        dark_mode_combo.grid(row=1, column=1, padx=10, pady=10)

        options3 = ["Normal contour", "Minimalist", "Drawing"]
        pieces_combo = self.create_combo(frame, options3)
        pieces_combo.bind('<<ComboboxSelected>>', lambda event: self.change_pieces(pieces_combo.get()))
        pieces_combo.grid(row=2, column=1, padx=10, pady=10)

        options4 = ["On", "Off"]
        transparent_combo = self.create_combo(frame, options4)
        transparent_combo.bind('<<ComboboxSelected>>', lambda event: self.set_transparent(transparent_combo.get()))
        transparent_combo.grid(row=3, column=1, padx=10, pady=10)

        new_root.transient(self.__root)
        new_root.grab_set()
        self.__root.wait_window(new_root)

        new_root.mainloop()

    def update(self):
        self.convert_board_to_interface()
        self.create_status_bars()

