import math

class Shape:
    def area(self):
        """
        Base method for calculating area.
        Raises NotImplementedError as it must be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        """
        return math.pi * (self.radius ** 2)