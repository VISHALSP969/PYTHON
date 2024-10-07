class Employee:
    """common base class for all employees"""
    # Class variable
    empCount = 0

    # Class constructor
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1

    # Class methods
    def displayCount(self):
        print(Employee.empCount)

    def displayEmployee(self):
        print('Name :', self.name, ' Salary :', self.salary, ' Age :', self.age)


# Creating instance objects
emp1 = Employee('Zara', 2000, 7)
emp2 = Employee('John', 5000, 8)

# Accessing attributes
emp1.displayEmployee()
emp2.displayEmployee()
print('Total Employee %d' % Employee.empCount)
