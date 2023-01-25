from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, length):
        pass


class RasterRender(Renderer):
    def render_circle(self, radius):
        print(f"Rendering raster circle with radius: {radius}")


class VectorVector(Renderer):
    def render_circle(self, radius):
        print(f"Rendering vector circle with radius: {radius}")


class Shape:
    def __init__(self, render):
        self.render = render

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, render, radius):
        super(Circle, self).__init__(render)
        self.radius = radius

    def draw(self):
        self.render.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

if __name__=="__main__":
    vector=VectorVector()
    raster=RasterRender()

    cirlce=Circle(vector,2)
    cirlce.draw()
    cirlce.resize(2)
    cirlce.draw()

