class Parent:
    def func1(self):
        print('This is function 1')


class Child(Parent):
    def func2(self):
        print('This is function 2')


obj = Child()
obj.func1()     # Inherited from Parent class
obj.func2()     # Defined in Child class
