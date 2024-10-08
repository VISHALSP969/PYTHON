class A:
    def method_A(self):
        print('Class A method')


class B(A):
    def method_B(self):
        print('Class B method')


class C(A):
    def method_C(self):
        print('Class C method')


class D(B, C):
    def method_D(self):
        print('Class D method')


obj = D()
obj.method_A()
obj.method_B()
obj.method_C()
obj.method_D()
