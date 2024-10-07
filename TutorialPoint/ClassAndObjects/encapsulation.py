class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print(f'Employee Name : {self.name} , Salary : {self.salary}')

    def set_salary(self, salary):
        if salary > 0:
            self.salary = salary
        else:
            print('Invalid salary!')


emp = Employee('John', 35000)
emp.display_employee()
emp.set_salary(60000)
emp.display_employee()
emp.set_salary(-4000)
emp.display_employee()

