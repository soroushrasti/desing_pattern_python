from typing import List


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
       self.propert_change=Event()

class Person(PropertyObservable):
    def __init__(self, age:int):
        super().__init__()
        self._age=age

    @property
    def can_vote(self):
        return self._age >18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        print(f"You are changing age to {age}")

        self.propert_change("age", age)
        self.propert_change("vote",age)
        self._age = age

class AuthorityTraffic:
     def __init__(self, person:Person):
         self.person=person
         self.person.propert_change.append(self.can_derive)
         self.person.propert_change.append(self.can_vote)

     def can_derive(self, attr, value):
       if attr == "age":
           if value<14:
               print(f"You are not allowed to drive")
           else:
               print("You can derive")
               self.person.propert_change.remove(self.can_derive)

     def can_vote(self, attr, age):
       if attr == "vote":
           if not self.person.can_vote:
               print(f"You are not allowed to vote")
           else:
               print("You can vote")
               self.person.propert_change.remove(self.can_vote)

if __name__ == '__main__':
    p=Person(2)
    at=AuthorityTraffic(p)
    for a in range(10, 22):
        # print(a)
        p.age=a