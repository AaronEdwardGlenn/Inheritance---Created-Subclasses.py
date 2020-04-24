# inheritence allows us to inherit attributes and methods from a parent class. Benefit of this is creating subclasses where we can gain funtionality from the parent clas, and then adjust, create, or modify functionality without affecting the parent class in any way.

# first we will create developers and managers. as they are good subclasses of employees. they will have all the things the employee class already has.


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

# we can give the developer class its own init method to instantiate all instances of it will defaults.


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        # NOTE super is required here to tell the code to find these other class attributes from the parent.
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

print(dev_1.email)
print(dev_2.email)

# method revolution order is the order in which python looks for class attributes. it first looks at the class itslef, then parent class (inherited class), then the builtins.

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.prog_lang)

print(mananger_1.pay)
mananger_1.apply_raise()
print(mananger_1.pay)

mananger_1.print_employees()
