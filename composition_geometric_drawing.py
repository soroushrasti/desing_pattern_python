

class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children=[]
        self._name="Geometry"
    @property
    def name(self):
        return self._name

    def __str__(self):
        items = self._print([],0)
        return " ".join(items)

    def _print(self, items, depth):
        stars="*"*depth
        items.append(stars)

        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")

        for c in self.children:
            c._print(items, depth+1)
            
        return items
class Square(GraphicObject):
     @property
     def name(self):
         return "Square"


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"

if __name__=="__main__":
    gd=GraphicObject()
    gd.children.append(Square("Red"))
    gd.children.append(Circle("Yellow"))
    group=GraphicObject()
    group._name="Group"
    group.children.append(Square("Purple"))
    group.children.append(Circle("While"))
    gd.children.append(group)
    print(gd)