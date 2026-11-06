
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def pay(self):
        return self.__salary

    def __str__(self):
        return f"Name: {self.name}, Pay: {self.pay()}"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def pay(self):
        return super().pay() + self.bonus


class Intern(Employee):
    def __init__(self, name, hours):
        super().__init__(name, 0)
        self.hours = hours

    def pay(self):
        return self.hours * 200


class Company:
    def __init__(self):
        self.people = []

    def add(self, person):
        self.people.append(person)

    def show_all(self):
        for person in self.people:
            print(person)

    def total_payroll(self):
        return sum(person.pay() for person in self.people)


company = Company()

asha = Employee("Asha", 30000)
rohit = Manager("Rohit", 50000, 8000)
kabir = Intern("Kabir", 80)

company.add(asha)
company.add(rohit)
company.add(kabir)

company.show_all()

print("Total Payroll:", company.total_payroll())
