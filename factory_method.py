from enum import Enum
from math import cos, sin


class COORDINATES(Enum):
    CARTESIAN=0
    POLAR=1

class Point:
    def __init__(self, a, b, system=COORDINATES.CARTESIAN):
       if system==COORDINATES.CARTESIAN:
           self.x= a
           self.y=b
       elif system == COORDINATES.POLAR:
           self.x = a * cos(b)
           self.y = a * sin(b)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
