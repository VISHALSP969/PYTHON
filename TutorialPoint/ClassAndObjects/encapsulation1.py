class Employee:
    def __init__(self, name, age, salary):
        self.name = name  # public attribute
        self._age = age  # protected attribute
        self.__salary = salary  # private attribute

    def display_public(self):
        print(f'Public - Name : {self.name}')

    def display_protected(self):
        print(f'Protected - Age : {self._age}')

    def display_private(self):
        print(f'Private - Salary : {self.__salary}')

    # public method to change private attribute
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print('Invalid salary!')


# create an object of the Employee class
emp = Employee('John', 30, 50000)

# public attributes and methods can be accessed directly
print('Accessing public attribute : ')
print(emp.name)
emp.display_public()

# protected attributes can be accessed (although not recommended)
print('\nAccessing protected attribute : ')
print(emp._age)
emp.display_protected()

# private attribute cannot be accessed directly from outside
print('\nAttempting to access private attribute : ')
# print(emp.__salary)       # Attribute error

# accessing private attribute via name mangling (not recommended)
print('\nAccessing private attribute via name mangling : ')
print(emp._Employee__salary)

# indirect access to private attributes via public method
print('\nAccessing private attribute via public method : ')
emp.display_private()

# changing private attribute using a public method
emp.set_salary(70000)
emp.display_private()
