from .shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, shape, radius, colour):
        super().__init__(shape, colour)
        self.radius = radius

    def area(self):
        return (pi * self.radius ** 2)

    def repr(self):
        print(f"Radius: {self.radius} \nColour: {self.shape_colour.colour}"
                    f" \nArea: {self.area()}")

    def print_shape(self):
        super().print_shape()