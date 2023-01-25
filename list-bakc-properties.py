

class Creature:
    _agility=0
    _creativity=1
    _inteligent=2
    def __init__(self):
        self.stats=[10,10,10]

    @property
    def agility(self):
        return self.stats[Creature._agility]

    @agility.setter
    def agility(self, value):
         self.stats[Creature._agility]=value


    @property
    def inteligent(self):
        return self.stats[Creature._inteligent]

    @inteligent.setter
    def inteligent(self, value):
         self.stats[Creature._inteligent]=value

    @property
    def creativity(self):
        return self.stats[Creature._creativity]

    @creativity.setter
    def creativity(self, value):
         self.stats[Creature._creativity]=value


    @property
    def sum(self):
        return sum(self.stats)


    @property
    def max(self):
        return sum(self.stats)


if __name__ == '__main__':
    c= Creature()
    print(c.agility)
    c.creativity=2000
    print(c.sum)