import random
import string


class User:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name


class User1:
    def __init__(self, first_name, last_name):
        self.strings = []

        def get_or_add(string):
            if string in self.strings:
                return self.strings.index(string)
            else:
                self.strings.append(string)
                return len(self.strings) - 1

        self.last_name = get_or_add(last_name)
        self.first_name = get_or_add(first_name)

    def __getattr__(self, item):
        if item=="first_name":
            print("item")
            return self.strings[self.first_name]
        if item=="last_name":
           return self.strings[self.last_name]
        return " "


    @property
    def name(self):
        return self.strings[self.first_name] + " " + self.strings[self.last_name]

    def __str__(self):
        return f"{self.strings[self.first_name]} {self.strings[self.last_name]}"

chars = string.ascii_lowercase


def random_string():
    return "".join([random.choice(chars) for i in range(5)])


if __name__ == '__main__':
    users=[]
    for first in [random_string() for i in range(100)]:
        for last in [random_string() for i in range(100)]:
            users.append(User1(first, last))
    print(users[0].name)
    print(users[0])


