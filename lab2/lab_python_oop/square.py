from .rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, shape, side, colour):
        super().__init__(shape, side, side, colour)

    # def area(self):
    #     super().area()
