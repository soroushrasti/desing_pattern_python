# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
from abstract_factory import HotDrinkMachine
from builder import HTMLBuilder
from builder_facet import PersonBuilder
from factory_method_1 import Point

if __name__ == '__main__':
    class Me:
        my_list=[1,2,3,4]

        def __iter__(self):
            return iter(self.my_list)
    for i in Me():
        print(i)
    # print(Me())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
