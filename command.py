from abc import ABC
from enum import Enum


class BankAccount:
    Withdraw_limit=-200

    def __init__(self, balance: int=0):
        self.balance=balance

    def deposit(self, amount:int)-> bool:
        self.balance+=amount
        return True

    def withdraw(self, amount:int)-> bool:
        if self.balance-amount< self.Withdraw_limit:
            return False
        self.balance-=amount
        return True

    def __str__(self):
         return f"balance={self.balance}"

class Command(ABC):
    def invoke(self):
       pass
    def undo(self):
        pass

class BankCommand(Command):
    class TypeAction(Enum):
        DEPOIST=0
        WITHDRAW=1

    def __init__(self, account: BankAccount, amount:int, action:TypeAction ):
        self.action = action
        self.amount = amount
        self.account = account
        self.success=None

    def invoke(self):
      if self.action == self.TypeAction.DEPOIST:
          self.success=self.account.deposit(self.amount)
      elif self.action == self.TypeAction.WITHDRAW:
          self.success = self.account.withdraw(self.amount)

    def undo(self)-> None:
        if not self.success:
            return
        if self.action == self.TypeAction.DEPOIST:
            self.account.withdraw(self.amount)
        elif self.action == self.TypeAction.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == '__main__':
    ba=BankAccount(0)
    print(ba)
    bc=BankCommand(ba,100,BankCommand.TypeAction.DEPOIST)
    bc.invoke()
    print(ba)
    bc.undo()
    print(ba)
    bc1=BankCommand(ba,1000,BankCommand.TypeAction.WITHDRAW)
    bc1.invoke()
    print(ba)
    bc1.undo()
    print(ba)


