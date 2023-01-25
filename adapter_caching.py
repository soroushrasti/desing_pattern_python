class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y

class DrawPoint:
    def __init__(self, p):
        # if p.x==0:
        #     print(".")
        # if p.y==0:
            print(".", end=" ")


class Line:
    def __init__(self, start, end):
        self.end = end
        self.start = start

class LineAdapter:
    cache = {}

    def __init__(self,line):
        self.h= hash(line)
        if self.h in self.cache:
            return

        super(LineAdapter, self).__init__()
        print("\nDrawing line\n")
        left= min(line.start.x, line.end.x)
        right= max(line.start.x, line.end.x)
        bottom= min(line.start.y, line.end.y)
        top= max(line.start.y, line.end.y)
        points=[]
        if left - right==0:
            for y in range(bottom, top):
                points.append(Point(0,y))
        elif top - bottom==0:
            for x in range(left, right):
                points.append(Point(x,0))

        self.cache[self.h]=points

    def __iter__(self):
        return iter(self.cache[self.h])

class Rectangular(list):
    def __init__(self, x,y, width, high):
        super().__init__()
        self.append(Line(Point(x,y), Point(x+width,y)))
        self.append(Line(Point(x,y), Point(x,y+high)))
        self.append(Line(Point(x+width,y), Point(x+width,y+high)))
        self.append(Line(Point(x,y+high), Point(x+width,y+high)))


if __name__=="__main__":
    rcs=[
        Rectangular(1,1,10,20),
        Rectangular(3,4,20,39)
    ]
    for rc in rcs:
        for line in rc:
            la=LineAdapter(line)
            for p in la:
                DrawPoint(p)


