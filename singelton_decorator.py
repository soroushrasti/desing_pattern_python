from random import randint

def singelton(class_):
    instances={}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_]=class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@singelton
class Database:
    def __init__(self):
        print(randint(1,1000))
        print("initializing database")


d1= Database()
d2 = Database()
print(d1==d2)
