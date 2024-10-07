class Father:
    def show_father(self):
        print('Father\'s method')


class Mother:
    def show_mother(self):
        print('Mother\'s method')


class Child(Father, Mother):
    def show_child(self):
        print('Child\'s method')


obj = Child()
obj.show_father()  # Father's method
obj.show_mother()  # Mother's method
obj.show_child()  # Child's method
