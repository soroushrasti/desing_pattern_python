from abc import ABC
from enum import Enum


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class WhatToQuery(Enum):
    ATTACK=1
    DEFENSE=2



class Query:
    def __init__(self,name: str, what_to_query:WhatToQuery, default_value:int):
        self.name = name
        self.what_to_query = what_to_query
        self.value = default_value

class Creature:
    def __init__(self, name:str, game, defense: int, attack:int ):
        self.init_attack = attack
        self.init_defense = defense
        self.game = game
        self.name = name

    @property
    def attack(self):
        q=Query(self.name,WhatToQuery.ATTACK,self.init_attack)
        self.game.perform_queries(self, q)
        return q.value

    @property
    def defense(self):
        q=Query(self.name,WhatToQuery.DEFENSE,self.init_defense)
        self.game.perform_queries(self, q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack} / {self.defense})"

class Game:
    def __init__(self):
        self.queries = Event()

    def perform_queries(self, sender: Creature, query: Query):
        self.queries(sender,query)

class CreatureModifier(ABC):
    def __init__(self, creature:Creature, game:Game):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender:Creature,query:Query):
       pass

class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender:Creature,query:Query):
        if self.creature.name == sender.name and query.what_to_query==WhatToQuery.ATTACK:
            query.value*=2



if __name__ == '__main__':
    g=Game()
    gablin=Creature("Goblin",g,1,1)
    print(gablin)
    dam=DoubleAttackModifier(gablin,g)
    DoubleAttackModifier(gablin,g)

    print(gablin)