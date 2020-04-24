# is instance is subclasses
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return('{}, {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    raise_amount = 1.8


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    raise_amount = 5

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employees in self.employees:
            print('-->', employees.fullname())


dev_1 = Developer('Aaron', 'Glenn', 100, 'Python')
dev_2 = Developer('Test', 'User', 200, 'Java')

mananger_1 = Manager('Calvin', 'Coolidge', 500, [dev_1])

print(isinstance(mananger_1, Developer))    # this tells us if an object in an instance of a class

print(issubclass(Manager, Employee))  # this tells us if an object is a subclass of a class.
