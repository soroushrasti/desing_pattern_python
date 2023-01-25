from typing import Optional


class Person:
    def __init__(self, name:str):
        self.name=name
        self.chat_logs:[str]=[]
        self.room: Optional['ChatRoom']=None

    def receive(self,sender:'Person', msg:str):
        m= f"{sender.name}: {msg}"
        print(f"{self.name} room: ",m)
        self.chat_logs.append(m)

    def private_message(self, reciever:'Person', msg:str):
        self.room.message(self,reciever,msg)


    def say(self, msg:str):
        self.room.broadcast(self,msg)

class ChatRoom:
    def __init__(self):
       self.people:[Person]=[]

    def join(self, who:Person):
        self.people.append(who)
        who.room=self
        self.broadcast(who, f"{who.name} has joined tha channel")


    def broadcast(self, source: Person, msg):
       for p in self.people:
          if p.name!= source.name:
              p.receive(source, msg)


    def message(self, sender:Person, receiver:Person, msg:str):
         for p in self.people:
             if p.name==receiver.name:
                 p.receive(sender,msg)


if __name__ == '__main__':
    chat=ChatRoom()

    john=Person("John")
    leyla=Person("Leyla")

    chat.join(john)
    chat.join(leyla)

    john.say("Hi team, I am saything publicly")

    leyla.private_message(john, "hey john, how are you?")

