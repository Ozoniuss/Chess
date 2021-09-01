from Domain.PieceTypes.PieceType import PieceType
from Domain.PieceColors.PieceColor import PieceColor

class ImagesColors:
    def __init__(self, frame):
        self.__frame = frame
        self.__image_path = 'Pictures/'

        self.__colors = {'board1': '#dcbfb4',
                         'board2': 'steel blue',
                         'when clicked2': 'SteelBlue2',
                         'when clicked1': 'MistyRose2',
                         'available position': 'AntiqueWhite1',
                         'frame' : 'gray20',
                         'button leave': 'gray27',
                         'button enter': 'gray36',
                         'text': 'white',
                         'status': 'gray36'
                        }

        self.__images = {(PieceType.PAWN, PieceColor.BLACK) : self.__image_path + 'black_pawn.png',
                         (PieceType.PAWN, PieceColor.WHITE): self.__image_path + 'white_pawn.png',
                         (PieceType.BISHOP, PieceColor.BLACK): self.__image_path + 'black_bishop.png',
                         (PieceType.BISHOP, PieceColor.WHITE): self.__image_path + 'white_bishop.png',
                         (PieceType.KNIGHT, PieceColor.BLACK): self.__image_path + 'black_knight.png',
                         (PieceType.KNIGHT, PieceColor.WHITE): self.__image_path + 'white_knight.png',
                         (PieceType.ROCK, PieceColor.BLACK): self.__image_path + 'black_rock.png',
                         (PieceType.ROCK, PieceColor.WHITE): self.__image_path + 'white_rock.png',
                         (PieceType.KING, PieceColor.BLACK): self.__image_path + 'black_king.png',
                         (PieceType.KING, PieceColor.WHITE): self.__image_path + 'white_king.png',
                         (PieceType.QUEEN, PieceColor.BLACK): self.__image_path + 'black_queen.png',
                         (PieceType.QUEEN, PieceColor.WHITE): self.__image_path + 'white_queen.png'
                         }

        self.__size = {'normal': (30, 50),
                       'drawing': (55, 65),
                       'minimalist': (55, 60),
                       'transparent': (50, 60)
                       }

        self.image_width = 30
        self.image_height = 50
        self.__transparent = False
        self.__type = 'normal'

    def get_image(self, type, color):
        return self.__images[(type, color)]

    def get_color(self, type):
        return self.__colors[type]

    def set_color(self, type, color):
        self.__colors[type] = color

    def dark_mode_colors(self):
        self.__colors['when clicked1'] = 'MistyRose2'
        self.__colors['available position'] = 'AntiqueWhite1'
        self.__colors['board1'] = '#dcbfb4'
        self.__colors['frame'] = 'gray20'
        self.__colors['button leave'] = 'gray27'
        self.__colors['button enter'] = 'gray36'
        self.__colors['text'] = 'white'
        self.__colors['status'] = 'gray36'

    def powder_mode_colors(self):
        self.__colors['when clicked1'] = '#efcfc6'
        self.__colors['available position'] = '#f9ebe8'
        self.__colors['board1'] = '#e3b4a6'
        self.__colors['frame'] = '#d7b19f'
        self.__colors['button leave'] = '#b57360'
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
            self.__colors['board2'] = "#8f0536"
            self.__colors['when clicked2'] = '#ee9193'

    def set_dark_mode(self, state):
        if state == "Powder":
            self.powder_mode_colors()
        else:
            self.dark_mode_colors()
        self.__frame.config(bg=self.__colors['frame'])

    def is_transparent(self):
        if self.__transparent:
            self.make_transparent()

    def set_pieces_drawing(self):
        self.__images = {(PieceType.PAWN, PieceColor.BLACK) : self.__image_path + 'black_pawn_dr.png',
                         (PieceType.PAWN, PieceColor.WHITE): self.__image_path + 'white_pawn_dr.png',
                         (PieceType.BISHOP, PieceColor.BLACK): self.__image_path + 'black_bishop_dr.png',
                         (PieceType.BISHOP, PieceColor.WHITE): self.__image_path + 'white_bishop_dr.png',
                         (PieceType.KNIGHT, PieceColor.BLACK): self.__image_path + 'black_knight_dr.png',
                         (PieceType.KNIGHT, PieceColor.WHITE): self.__image_path + 'white_knight_dr.png',
                         (PieceType.ROCK, PieceColor.BLACK): self.__image_path + 'black_rock_dr.png',
                         (PieceType.ROCK, PieceColor.WHITE): self.__image_path + 'white_rock_dr.png',
                         (PieceType.KING, PieceColor.BLACK): self.__image_path + 'black_king_dr.png',
                         (PieceType.KING, PieceColor.WHITE): self.__image_path + 'white_king_dr.png',
                         (PieceType.QUEEN, PieceColor.BLACK): self.__image_path + 'black_queen_dr.png',
                         (PieceType.QUEEN, PieceColor.WHITE): self.__image_path + 'white_queen_dr.png'
                         }
        self.__type = 'drawing'
        self.image_width, self.image_height = self.__size[self.__type]
        self.is_transparent()

    def set_pieces_normal(self):
        self.__images = {(PieceType.PAWN, PieceColor.BLACK) : self.__image_path + 'black_pawn.png',
                         (PieceType.PAWN, PieceColor.WHITE): self.__image_path + 'white_pawn.png',
                         (PieceType.BISHOP, PieceColor.BLACK): self.__image_path + 'black_bishop.png',
                         (PieceType.BISHOP, PieceColor.WHITE): self.__image_path + 'white_bishop.png',
                         (PieceType.KNIGHT, PieceColor.BLACK): self.__image_path + 'black_knight.png',
                         (PieceType.KNIGHT, PieceColor.WHITE): self.__image_path + 'white_knight.png',
                         (PieceType.ROCK, PieceColor.BLACK): self.__image_path + 'black_rock.png',
                         (PieceType.ROCK, PieceColor.WHITE): self.__image_path + 'white_rock.png',
                         (PieceType.KING, PieceColor.BLACK): self.__image_path + 'black_king.png',
                         (PieceType.KING, PieceColor.WHITE): self.__image_path + 'white_king.png',
                         (PieceType.QUEEN, PieceColor.BLACK): self.__image_path + 'black_queen.png',
                         (PieceType.QUEEN, PieceColor.WHITE): self.__image_path + 'white_queen.png'
                         }
        self.__type = 'normal'
        self.image_width, self.image_height = self.__size[self.__type]
        self.is_transparent()

    def set_pieces_minimalist(self):
        self.__images = {(PieceType.PAWN, PieceColor.BLACK) : self.__image_path + 'black_pawn_minimalist.png',
                         (PieceType.PAWN, PieceColor.WHITE): self.__image_path + 'white_pawn_minimalist.png',
                         (PieceType.BISHOP, PieceColor.BLACK): self.__image_path + 'black_bishop_minimalist.png',
                         (PieceType.BISHOP, PieceColor.WHITE): self.__image_path + 'white_bishop_minimalist.png',
                         (PieceType.KNIGHT, PieceColor.BLACK): self.__image_path + 'black_knight_minimalist.png',
                         (PieceType.KNIGHT, PieceColor.WHITE): self.__image_path + 'white_knight_minimalist.png',
                         (PieceType.ROCK, PieceColor.BLACK): self.__image_path + 'black_rock_minimalist.png',
                         (PieceType.ROCK, PieceColor.WHITE): self.__image_path + 'white_rock_minimalist.png',
                         (PieceType.KING, PieceColor.BLACK): self.__image_path + 'black_king_minimalist.png',
                         (PieceType.KING, PieceColor.WHITE): self.__image_path + 'white_king_minimalist.png',
                         (PieceType.QUEEN, PieceColor.BLACK): self.__image_path + 'black_queen_minimalist.png',
                         (PieceType.QUEEN, PieceColor.WHITE): self.__image_path + 'white_queen_minimalist.png'
                         }
        self.__type = 'minimalist'
        self.image_width, self.image_height = self.__size[self.__type]
        self.is_transparent()

    def check_transparent(self):
        if not self.__transparent:
            self.make_transparent()

    def check_full(self):
        if self.__transparent:
            self.make_full()

    def make_transparent(self):
        for key in self.__images:
            self.__images[key] = self.__images[key][:-4]
            self.__images[key] += '_tr' + '.png'
        self.__transparent = True
        self.image_width, self.image_height = self.__size['transparent']

    def make_full(self):
        for key in self.__images:
            self.__images[key] = self.__images[key][:-7]
            self.__images[key] += '.png'
        self.__transparent = False
        self.image_width, self.image_height = self.__size[self.__type]


