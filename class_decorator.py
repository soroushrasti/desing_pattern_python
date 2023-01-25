from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ""

class Circle(Shape):
     def __init__(self, radius):
         self.radius = radius

     def resize(self, factor):
         self.radius*=factor

     def __str__(self):
         return f"Circle has {self.radius} radius"

class Square(Shape):
     def __init__(self, side):
         self.side=side

     def __str__(self):
         return f"Square has {self.side} side"

class ColoredShape(Shape):
     def __init__(self, shape, color):
         self.color = color
         self.shape = shape

     def __str__(self):
         return f"{self.shape} and {self.color} color"


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.transparency = transparency
        self.shape = shape

    def __str__(self):
        return f"{self.shape} and {self.transparency*100}% transparency"

if __name__ == '__main__':
    circle=Circle(2)
    circle.resize(2)
    print(circle)
    red_circle=ColoredShape(circle,"red")
    red_circle.resize(2)
    print(red_circle)
    half_transparent_red_circle=TransparentShape(red_circle,0.5)

    print(half_transparent_red_circle)