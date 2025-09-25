from abc import ABC, abstractmethod
from .shape_colour import Shape_colour


class Shape(ABC):
    def __init__(self, shape, colour):
        self.shape = shape
        self.shape_colour = Shape_colour(colour)

    def print_shape(self):
        print(f"Фигура: {self.shape}")

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def repr(self):
        pass
