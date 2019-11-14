# Alex C - location.py class

class Location():

    def __init__(self, address=""):
        self.address = address

    def __str__(self):
        return f"Location: {self.address}"


class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Business(Location):

    def __init__(self, name, address):
        super().__init__(address)
        self.name = name
        self.employees = []
 
    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return f"{self.name}, {len(self.employees)} employees"


class Home(Location):

    def __init__(self, address):
        super().__init__(address)
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)

    def resident_names(self):
        list_residents = []
        for person in self.residents:
            list_residents.append(str(person.first_name)+" "+person.last_name)
        return list_residents

    def __str__(self):
        return f"{self.address}, {len(self.residents)} residents"