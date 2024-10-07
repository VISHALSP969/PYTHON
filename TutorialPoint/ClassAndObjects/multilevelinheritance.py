class Grandparent:
    def show_grandparent(self):
        print('Grandparent\'s method')


class Parent(Grandparent):
    def show_parent(self):
        print('Parent\'s method')


class Child(Parent):
    def show_child(self):
        print('Child\'s method')


obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()
