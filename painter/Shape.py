from Point import Point
from Colour3 import Colour3

##holds information about that point, such as position, colour, size, and what shape this point is attached to
class Shape:
    Location = Point(0,0)
    Width = 0.0
    Colour = Colour3(0,0,0)
    ShapeNumber = 0
    #CONSTRUCTOR - with the values to give it
    def __init__(self, L, W, C, S):
        self.Location = L
        self.Width = W
        self.Colour = C
        self.ShapeNumber = S