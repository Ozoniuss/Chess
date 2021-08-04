from abc import ABC, abstractmethod
from tkinter import *
from PIL import ImageTk, Image


class StatusPiece:
    def __init__(self, type, color, pixels):
        self.__type = type
        self.__color = color
        self.__pixels = pixels

    def get_type(self):
        return self.__type

    def get_color(self):
        return self.__color

    def get_pixels(self):
        return self.__pixels

    def set_pixels(self, pixels):
        self.__pixels = pixels

    def increase_pixels(self, pixels):
        self.__pixels += pixels


class StatusBar(ABC):
    def __init__(self, frame, images_colors):
        pass
        self._frame = frame
        self._images_colors = images_colors
        self._canvas = None
        self._pixels = 100
        self._status_size = 20
        self._status_size_overlap = 7
        self._status_bar = {'pawn': [],
                                   'bishop': [],
                                   'knight': [],
                                   'rock': [],
                                   'queen': [],
                                   'king': []
                                   }
        self._pieces ={'pawn' : [],
                        'bishop': [],
                        'knight': [],
                        'rock': [],
                        'queen': [],
                        'king': []
                        }
        self._photo_references = []

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

    def switch_pieces_one_pos(self, type):
        # Because we want the pieces of the same kind to overlap, the amount of pixels
        # that the following pieces are moved depends if we have any pieces of "type" already out

        pieces_to_be_moved = self.get_greater_pieces(type)
        number_pieces_moved = 0
        pixels = self._status_size
        if len(self._status_bar[type]) != 0:
            pixels = self._status_size_overlap
        for piece_type in pieces_to_be_moved:
            for piece_drawing in self._status_bar[piece_type]:
                self._canvas.move(piece_drawing, pixels, 0)
                number_pieces_moved += 1
            for element in self._pieces[piece_type]:
                element.increase_pixels(pixels)

        return number_pieces_moved, pixels

    def get_piece_out(self, color, type):

        # because we want to keep the pieces in order, we get a list of types of the pieces
        # that we move one position to the right
        number_pieces_moved, pixels = self.switch_pieces_one_pos(type)

        img = Image.open(self._images_colors.get_image(type, color))
        self._photo_references.append(ImageTk.PhotoImage(img.resize((15, 20), Image.ANTIALIAS)))
        image = self._canvas.create_image(
            (self._pixels - self._status_size * number_pieces_moved) + pixels, 20,
            image=self._photo_references[len(self._photo_references) - 1])
        self._status_bar[type].append(image)
        element_pixels = (self._pixels - self._status_size * number_pieces_moved) + pixels
        piece = StatusPiece(type, color, element_pixels)
        self._pixels += pixels
        self._pieces[type].append(piece)

    @abstractmethod
    def create_status_bar(self, orientation): pass

    @abstractmethod
    def reverse(self, orientation): pass


class WhiteStatusBar(StatusBar):
    def __init__(self, frame, images_colors):
        super(WhiteStatusBar, self).__init__(frame, images_colors)

    def create_status_bar(self, orientation):
        self._canvas = Canvas(self._frame, width=641, height=40, highlightthickness=0,
                               bg=self._images_colors.get_color('status'))
        self._canvas.create_text(55, 20, text="Black player", fill="Black", font=('MS Serif', 13))
        if orientation == 'wd':
            self._canvas.grid(row=1, column=1, padx=(50, 0), pady=10, sticky=S)
        else:
            self._canvas.grid(row=34, column=1, padx=(50, 0), pady=10, sticky=S)

        for key in self._pieces:
            for element in self._pieces[key]:
                type = element.get_type()
                color = element.get_color()
                img = Image.open(self._images_colors.get_image(type, color))
                self._photo_references.append(ImageTk.PhotoImage(img.resize((15, 20), Image.ANTIALIAS)))
                self._canvas.create_image(element.get_pixels(), 20,
                                            image=self._photo_references[len(self._photo_references) - 1])

    def reverse(self, orientation):
        if orientation == "wd":
            self._canvas.grid(row=1, column=1, padx=(50, 0), pady=10, sticky=S)
        else:
            self._canvas.grid(row=34, column=1, padx=(50, 0), pady=10, sticky=S)


class BlackStatusBar(StatusBar):
    def __init__(self, frame, images_colors):
        super(BlackStatusBar, self).__init__(frame, images_colors)

    def create_status_bar(self, orientation):
        self._canvas = Canvas(self._frame, width=641, height=40, highlightthickness=0,
                               bg=self._images_colors.get_color('status'))
        self._canvas.create_text(55, 20, text="White player", fill="White", font=('MS Serif', 13))
        if orientation == 'wd':
            self._canvas.grid(row=34, column=1, padx=(50, 0), pady=10, sticky=S)
        else:
            self._canvas.grid(row=1, column=1, padx=(50, 0), pady=10, sticky=S)

        for key in self._pieces:
            for element in self._pieces[key]:
                type = element.get_type()
                color = element.get_color()
                img = Image.open(self._images_colors.get_image(type, color))
                self._photo_references.append(ImageTk.PhotoImage(img.resize((15, 20), Image.ANTIALIAS)))
                self._canvas.create_image(element.get_pixels(), 20,
                                            image=self._photo_references[len(self._photo_references) - 1])

    def reverse(self, orientation):
        if orientation == "wd":
            self._canvas.grid(row=34, column=1, padx=(50, 0), pady=10, sticky=S)
        else:
            self._canvas.grid(row=1, column=1, padx=(50, 0), pady=10, sticky=S)

