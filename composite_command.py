import unittest
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
    def __init__(self):
        self.success = None

    def invoke(self):
       pass
    def undo(self):
        pass

class BankCommand(Command):
    class TypeAction(Enum):
        DEPOIST=0
        WITHDRAW=1

    def __init__(self, account: BankAccount, amount:int, action:TypeAction ):
        super(BankCommand, self).__init__()
        self.action = action
        self.amount = amount
        self.account = account


    def invoke(self):
      if self.action == self.TypeAction.DEPOIST:
          self.success=self.account.deposit(self.amount)
      elif self.action == self.TypeAction.WITHDRAW:
          self.success = self.account.withdraw(self.amount)
      return self.success

    def undo(self)-> None:
        if not self.success:
            return
        if self.action == self.TypeAction.DEPOIST:
            self.account.withdraw(self.amount)
        elif self.action == self.TypeAction.WITHDRAW:
            self.account.deposit(self.amount)

class CompositeBankdCommand(Command, list):
    def __init__(self, items:[Command]):
        super().__init__()
        for x in items:
            self.append(x)

    def invoke(self):
       for x in self:
         x.invoke()

    def undo(self):
       for x in reversed(self):
           x.undo()

class TransferAccount(CompositeBankdCommand):
     def __init__(self, from_acc, into_acc, amount):
         super(TransferAccount, self).__init__(
             [
                 BankCommand(from_acc,amount,BankCommand.TypeAction.WITHDRAW),
                 BankCommand(into_acc, amount, BankCommand.TypeAction.DEPOIST),
             ]
         )

     def invoke(self):
         ok=True
         for x in self:
           if ok:
              ok= x.invoke()
         self.success=ok

     def undo(self):
         ok=True
         for x in reversed(self):
           if ok:
              ok= x.undo()
         self.success=ok


class TestSuite(unittest.TestCase):
    def test_deposit(self):
        ba = BankAccount(0)
        bc = BankCommand(ba, 100, BankCommand.TypeAction.DEPOIST)
        bc.invoke()
        self.assertEqual(ba.balance, 100)

    def test_withdraw(self):
        ba = BankAccount(0)
        bc = BankCommand(ba, 100, BankCommand.TypeAction.WITHDRAW)
        bc.invoke()
        self.assertEqual(ba.balance, -100)

    def test_multiple_deposit(self):
        ba = BankAccount(0)
        bc1 = BankCommand(ba, 100, BankCommand.TypeAction.DEPOIST)
        bc2=BankCommand(ba, 300, BankCommand.TypeAction.DEPOIST)
        cbc=CompositeBankdCommand([bc1,bc2])
        cbc.invoke()
        self.assertEqual(ba.balance,400)

    def test_transer_valid(self):
        ba1 = BankAccount(200)
        ba2 = BankAccount(0)
        TransferAccount(ba1,ba2,200).invoke()
        self.assertEqual(ba1.balance+200,ba2.balance)

    def test_transer_invalid(self):
        ba1 = BankAccount(200)
        ba2 = BankAccount(0)
        TransferAccount(ba1,ba2,1000).invoke()
        self.assertEqual(ba1.balance,200)
        self.assertEqual(ba2.balance,0)

if __name__ == '__main__':
    unittest.main()



