from random import randint


class Database:
    _instance=None
    def __init__(self):
        print(randint(1,1000))
        print("initializing database")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
           cls._instance= super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

d1= Database()
d2 = Database()
print(d1==d2)
