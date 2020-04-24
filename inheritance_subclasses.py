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
        self.pay = int(self.pay * Employee.raise_amount)


class Developer(Employee):
    pass


dev_1 = Employee('Aaron', 'Glenn', 100)
dev_2 = Employee('Test', 'User', 200)

print(dev_1.email)
print(dev_2.email)
