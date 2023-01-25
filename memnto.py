from typing import List


class Memento:
    def __init__(self, balance: int):
        self.balance=balance

class BankAccount:
    def __init__(self, balance=0):
        self.balance=balance
        self.chages:List[Memento]=[Memento(self.balance)]
        self.current=0

    def deposit(self, amount: int):
        self.balance+=amount
        m= Memento(self.balance)
        self.chages.append(m)
        self.current+=1
        return m

    def restore(self,memento:Memento=None, current:int=None):
        if memento:
            self.chages.append(memento)
            self.current=len(self.chages)-1
        if current:
            self.balance=self.chages[current].balance
            self.current=current
    def undo(self):
        if self.current>0:
            self.current-=1
            m= self.chages[self.current]
            self.balance=m.balance
            return m
        return None
    def redo(self):
        if self.current<len(self.chages)-1:
            self.current+=1
            m= self.chages[self.current]
            self.balance=m.balance
            return m
        return None
    def __str__(self):
        return f"Bank with balance: {self.balance}"

if __name__ == '__main__':
    ba=BankAccount(100)
    ba.deposit(50)
    ba.deposit(30)

    print(ba)
    print(ba.current)
    ba.restore(1)
    print(ba)