from collections import  Iterable
from abc import ABC


class Connectable(ABC, Iterable):
    def connect_to(self, other):
        if self==other:
            return

        for s in self:
            for o in other:
                s.inputs.append(o)
                o.outputs.append(s)

class Neuron(Connectable):
    def __init__(self, name):
        self.inputs=[]
        self.outputs=[]
        self.name=name

    def __str__(self):
        return f"Neuron {self.name} has {len(self.inputs)} inputs and {len(self.outputs)}"

    def __iter__(self):
        yield self

class NeuralLayer(list, Connectable):
    def __init__(self, name, count):
        super(NeuralLayer, self).__init__()
        self.name=name
        for i in range(count):
            self.append(Neuron(f"{name}-{i}"))

    def __str__(self):
        return f"layer {self.name} has {len(self)} neurons"

if __name__=="__main__":
    n1=Neuron("neuron1")
    n2=Neuron("neuron2")

    l1=NeuralLayer("Layer", 3)
    l2=NeuralLayer("Layer", 5)

    n1.connect_to(n2)
    n2.connect_to(l1)
    l1.connect_to(l2)

    print(n1)
    print(n2)
    print(l1)
    print(l2)

