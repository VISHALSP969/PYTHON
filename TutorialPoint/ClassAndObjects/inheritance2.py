class Parent:
    def myMethod(self):
        print('Calling parent method')


class Child(Parent):
    def myMethod(self):
        print('Calling child method')


c = Child()  # instance of child
c.myMethod()  # child calls overridden method
