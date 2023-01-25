from typing import List


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Person:
    def __init__(self, name: str, address: str):
        self.address = address
        self.name = name
        self.falls_ill=Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)

class Doctor:
    def __init__(self, persons:List[Person]):
         self.persons = persons
         for p in self.persons:
             p.falls_ill.append(self.notify_doctor)

    def notify_doctor(self, name, address):
        print(f"I am notified that {name} at {address} is ill")



if __name__ == '__main__':
    p1=Person("John", "London")
    p2=Person("Messy", "Spain")

    p1.falls_ill.append(lambda name, address: print(f"perons {name} at {address} is ill"))
    Doctor([p1,p2])
    p1.catch_a_cold()
