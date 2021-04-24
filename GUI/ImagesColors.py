
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
        self.__images = {('pawn', 'black') : self.__image_path + 'black_pawn.png',
                         ('pawn', 'white'): self.__image_path + 'white_pawn.png',
                         ('bishop', 'black'): self.__image_path + 'black_bishop.png',
                         ('bishop', 'white'): self.__image_path + 'white_bishop.png',
                         ('knight', 'black'): self.__image_path + 'black_knight.png',
                         ('knight', 'white'): self.__image_path + 'white_knight.png',
                         ('rock', 'black'): self.__image_path + 'black_rock.png',
                         ('rock', 'white'): self.__image_path + 'white_rock.png',
                         ('king', 'black'): self.__image_path + 'black_king.png',
                         ('king', 'white'): self.__image_path + 'white_king.png',
                         ('queen', 'black'): self.__image_path + 'black_queen.png',
                         ('queen', 'white'): self.__image_path + 'white_queen.png'
                         }

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

