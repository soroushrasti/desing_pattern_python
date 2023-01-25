import unittest


class Singeleton(type):
    _instances={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls]=super(Singeleton, cls).__call__(*args, **kwargs)
        return  cls._instances[cls]

class Database(metaclass=Singeleton):
    def __init__(self):
         self.cities={}

         print("reading database file")
         file = open("countries.txt", 'r')
         lines=file.readlines()
         for i in range(0, len(lines)-1,2):
             self.cities[lines[i].strip()]=int(lines[i+1].strip())
         file.close()

class SingeletonRecordFinder:
    def totol_population(self, cities):
        result=0
        for c in cities:
            if c in Database().cities:
                result+=Database().cities[c]
        return result

class ConfurableRecordFinder:
    def __init__(self, db):
        self.db=db

    def totol_population(self, cities):
        result = 0
        for c in cities:
            if c in self.db.cities:
                result += self.db.cities[c]
        return result

class FakeDatabase:
    cities={
        "alpha":10,
        "beta":20
    }
class SingeltonTest(unittest.TestCase):
    def test_is_singeltion(self):
        rf=SingeletonRecordFinder()
        self.assertEqual(rf.totol_population(["Tehran"]), 1000)
        self.assertEqual(rf.totol_population(["Tehran", "Esfahan"]), 3000)
    def test_configrable_database(self):
        crf=ConfurableRecordFinder(db=FakeDatabase)
        print(crf.totol_population(["alpha", "beta"]))
        self.assertEqual(crf.totol_population(["alpha", "beta"]), 30)

if __name__== "__main__":
    print("test started")
    unittest.main()
