from tkinter import *
from PIL import ImageTk, Image
from Domain.Pieces.Queen import Queen
from Domain.Pieces.Knight import Knight
from Domain.Pieces.Rock import Rock
from Domain.Pieces.Bishop import Bishop
from Domain.Pieces.EmptyPiece import EmptyPiece
from functools import partial


class PromotionTab:
    def __init__(self, root, frame, images_colors):
        self.__new_root = Toplevel(root)
        self.__new_root.withdraw()
        self.__new_root.protocol("WM_DELETE_WINDOW", self.replace_x)
        self.__photo_references = []
        self.__promotion_piece = EmptyPiece()
        self.__height = 70
        self.__width = 70
        self.__images_colors = images_colors

        # self.__new_root.transient(root)
        # self.__new_root.grab_set()
        # root.wait_window(self.__new_root)

    def replace_x(self):
        self.__new_root.withdraw()

    def show(self):
        self.__new_root.deiconify()

    def hide(self):
        self.__new_root.withdraw()

    def get_promotion_piece(self):
        return self.__promotion_piece

    @staticmethod
    def on_enter(button, color):
        button['background'] = color

    @staticmethod
    def on_leave(button, color):
        button['background'] = color

    @staticmethod
    def on_leave_standard(button, color):
        button['background'] = color

    def create_button_promotion(self, frame, type, color, bg, active_bg, first_color, second_color):
        img = Image.open(self.__images_colors.get_image(type, color))
        self.__photo_references.append(ImageTk.PhotoImage(img.resize((50, 60), Image.ANTIALIAS)))
        button = Button(frame, image = self.__photo_references[len(self.__photo_references)-1], height=self.__height,
                        width= self.__width, bg=bg, activebackground=active_bg, borderwidth=0)
        button.bind("<Enter>", lambda event, b = button: self.on_leave(b, first_color))
        button.bind("<Leave>", lambda event, b = button: self.on_leave_standard(b, second_color))
        return button

    def promotion_chosen(self, piece):
        # a promotion piece was chosen, so we net to set it to the attribute and destroy the Promotion tab
        self.__promotion_piece = piece
        self.__new_root.quit()

    def promotion_tab(self, piece_color, frame_color, bg, active_bg, first_color, second_color):
        self.show()
        self.__new_root.title("Promotion")
        self.__new_root.resizable(False, False)
        frame = Frame(self.__new_root, width=280, height=70, bg=frame_color)
        frame.grid(row=0, column=0)
        frame.grid_propagate(False)

        button_queen = self.create_button_promotion(frame, 'queen', piece_color, bg, active_bg, first_color, second_color)
        frame.grid(row=0, column=0)
        button_queen.grid(row=0, column=0, sticky=NW)
        button_queen.config(command=partial(self.promotion_chosen, Queen(piece_color)))

        button_knight = self.create_button_promotion(frame, 'knight', piece_color, bg, active_bg, first_color, second_color)
        button_knight.grid(row=0, column=1, sticky=NW)
        button_knight.config(command = partial(self.promotion_chosen, Knight(piece_color)))

        button_rock = self.create_button_promotion(frame, 'rock', piece_color, bg, active_bg, first_color, second_color)
        button_rock.grid(row=0, column=2, sticky=NW)
        button_rock.config(command = partial(self.promotion_chosen, Rock(piece_color)))

        button_bishop = self.create_button_promotion(frame, 'bishop', piece_color, bg, active_bg, first_color, second_color)
        button_bishop.grid(row=0, column=3, sticky=NW)
        button_bishop.config(command = partial(self.promotion_chosen, Bishop(piece_color)))

        self.__new_root.mainloop()