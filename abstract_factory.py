from abc import ABC
from enum import Enum


class HotDrink(ABC):
    def consume(self):
        pass


class Coffee(HotDrink):
    def consume(self):
        print("Enjoy your coffee!")


class Tea(HotDrink):
    def consume(self):
        print("Enjoy your tea!")


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"preparing {amount}ml coffee")
        return Coffee()

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"preparing {amount}ml tea")
        return Tea()

class HotDrinkMachine:
    class Drinks(Enum):
        COFFEE= 1
        TEA=2
    factories=[]
    def __init__(self):
        for d in self.Drinks:
            name= d.name[0] + d.name[1:].lower()
            instance= eval(name + "Factory()")
            self.factories.append((name, instance))
    def make_drink(self):
         for d in self.factories:
             print(d[0])
         drink=input("Choose you drink:")
         idx=int(drink)
         amount=input("Type the amount:")
         amount=float(amount)
         return self.factories[idx][1].prepare(amount).consume()


