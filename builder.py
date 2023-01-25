

class HTMLElement:
    indent_size=3
    def __init__(self, name="", text=""):
        self.name=name
        self.text=text
        self.elements=[]

    def __str(self, indentation=0):
        lines=[]
        i= " "*indentation*(self.indent_size)
        lines.append(f"{i}<{self.name}>")
        if self.text:
            i1=" "*(indentation+1)*(self.indent_size)
            lines.append(f"{i1}{self.text}")
        for e in self.elements:
            lines.append(e.__str(indentation+1))
        lines.append(f"{i}</{self.name}>")

        return "\n".join(lines)

    def __str__(self):
       return self.__str(0)

    @staticmethod
    def create(name):
        return HTMLBuilder(name)

class HTMLBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self._root = HTMLElement(root_name)
    def add_child(self, child_name, child_text):
        self._root.elements.append(HTMLElement(child_name, child_text))

    def add_child_fluent(self, child_name, child_text):
        self._root.elements.append(HTMLElement(child_name, child_text))
        return self
    def __str__(self):
        return str(self._root)
