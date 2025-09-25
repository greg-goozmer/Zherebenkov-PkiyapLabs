from .shape import Shape

class Rectangle(Shape):

    def __init__(self, shape, width, height, colour):
        super().__init__(shape, colour)
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def repr(self):
        print(f"Width: {self.width} \nHeight: {self.height} \nColour:"
              f" {self.shape_colour.colour} \nArea: {self.area()}")

    def print_shape(self):
        super().print_shape()


