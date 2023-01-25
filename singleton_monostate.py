class MonoState:
    shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(MonoState, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.shared_state
        return obj


class CEO(MonoState):
    def __init__(self):
        self.name=""
        self.managed_money=0

    def __str__(self):
        return f"{self.name} manages ${self.managed_money}"

c1=CEO()
c1.name="me"
c1.managed_money=123
print(c1)
c2=CEO()
c2.name="John"
c2.managed_money=100
print(c1)
print(c2)