from typing import List


class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer: List):
            buffer.append(str(self.value))

    def eval(self):
        return self.value

class AdditionExpression:
       def __init__(self, l, r):
           self.right =l
           self.left =r

       def print(self, buffer: List):
            buffer.append("(")
            self.left.print(buffer)
            buffer.append("+")
            self.right.print(buffer)
            buffer.append(")")
       def eval(self):
           return self.left.eval() + self.right.eval()
if __name__ == '__main__':
        e = AdditionExpression (DoubleExpression(1), AdditionExpression(DoubleExpression(2), DoubleExpression(3)))
        b=[]
        e.print(b)
        print(b)
        print(" ".join(b))
        print(e.eval())