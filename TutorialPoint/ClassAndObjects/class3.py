class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1

    def displayEmployee(self):
        print('Name :', self.name, ' Salary :', self.salary, ' Age :', self.age)

    def displayCount(self):
        print('Total employee %d' % Employee.empCount)


emp1 = Employee('Zara', 2000, 7)
emp1.displayEmployee()

print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
