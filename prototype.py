from copy import copy, deepcopy


class Address:
    def __init__(self, street, suit, country):
        self.country = country
        self.suit = suit
        self.street = street

    def __str__(self):
        return f"{self.street} suit # {self.suit} {self.country}"


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
       return f"{self.name} works at {self.address}"


class EmployeeFactory:
    main_office_employee= Employee("", Address("123 London", 0, "UK"))
    aux_office_employee= Employee("", Address("123B London", 0, "UK"))

    @staticmethod
    def __new_employee(prot,name, suit):
        employee=deepcopy(prot)
        employee.address.suit=suit
        employee.name=name
        return employee

    @staticmethod
    def new_aux_office_employee(name, suit):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suit
        )
    @staticmethod
    def new_main_office_employee(name, suit):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.new_main_office_employee,
            name, suit
        )
address= Address("123 London road", "123", "UK")
p = Employee("John", address)
print(p)
print("-----")
k= deepcopy(p)
k.address.street="124 London road"
print(p)
print(k)