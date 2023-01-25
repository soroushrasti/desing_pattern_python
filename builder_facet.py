

class Person:
    def __init__(self):
        # job
        self.salary = None
        self.position = None
        self.job_address = None
        # home
        self.phone = None
        self.home_address = None

    def __str__(self):
        return f"This person has a title with {self.position} with salary {self.salary}" \
               f"this person is living at {self.home_address} with phone {self.phone}"


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def lives(self):
        return HomePersonBuilder(self.person)

    @property
    def works(self):
        return JobPersonBuilder(self.person)

    def build(self):
       return self.person

class JobPersonBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def salary(self, salary):
       self.person.salary=salary
       return self


    def position(self, position):
        self.person.position = position
        return self
    def job_address(self, job_address):
        self.person.job_address = job_address
        return self

class HomePersonBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def phone(self, phone):
       self.person.phone=phone
       return self

    def position(self, home_address):
        self.person.home_address = home_address
        return self
