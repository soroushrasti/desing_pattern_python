


class Node:
    def __init__(self, value, left:'Node'=None, right:'Node'=None):
        self.value = value
        self.left = left
        self.right = right

        self.parent=None

        if self.right:
            self.right.parent=self

        if self.left:
            self.left.parent=self


def iterator(root:Node):
     def iterate(current:Node):
         if current.left:
             for r in iterate(current.left):
                 yield r

         yield current
         if current.right:
             for l in iterate(current.right):
                 yield l

     for current in iterate(root):
         yield current

"""
        1
       / \
     2    3
    / \
   4   5
"""
if __name__ == '__main__':
    root=Node(1, Node(2, Node(4), Node(5)), Node(3))

    for r in iterator(root):
        print(r.value)