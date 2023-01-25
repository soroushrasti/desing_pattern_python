from enum import Enum
from math import cos, sin


class COORDINATES(Enum):
    CARTESIAN = 0
    POLAR = 1


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    class PointFactory:
        def create_cartesian_point(self, x, y):
            return Point(x,y)

        def creat_polar_point(self, a,b):
            return Point(a * cos(b),a * sin(b))

    factory = PointFactory()