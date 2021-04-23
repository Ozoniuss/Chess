
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
