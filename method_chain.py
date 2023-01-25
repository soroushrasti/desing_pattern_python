from typing import Optional


class Creature:
    def __init__(self, name, attack, defense):
        self.defense = defense
        self.attack = attack
        self.name = name
    def __str__(self):
       return f"{self.name} ({self.attack}/{self.defense})"

class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.modifier: Optional[CreatureModifier]=None

    def add_modifier(self, modifier):
        if self.modifier:
            self.modifier.add_modifier(modifier)
        else:
           self.modifier=modifier

    def handle(self):
       if self.modifier:
           self.modifier.handle()

class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print("double the attack power")
        self.creature.attack*=2
        # print(self)
        # print(super().handle)
        super().handle()

class IncreaseOneDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack>10:
            print("increasing the defense by one")
            self.creature.defense+=1
        super().handle()

class NoBonusModifier(CreatureModifier):
    def handle(self):
       print("No bonus for you")

if __name__ == '__main__':
    gablin=Creature("Gabin",1,1)
    print(gablin)
    cm=CreatureModifier(gablin)
    cm.add_modifier(DoubleAttackModifier(gablin))
    cm.add_modifier(DoubleAttackModifier(gablin))
    cm.add_modifier(NoBonusModifier(gablin))
    cm.add_modifier(DoubleAttackModifier(gablin))
    cm.add_modifier(DoubleAttackModifier(gablin))
    cm.add_modifier(IncreaseOneDefenseModifier(gablin))
    cm.handle()

    print(gablin)