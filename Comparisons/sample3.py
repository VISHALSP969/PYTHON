class Foo(object):
    def __init__(self, item):
        self.my_item = item

    def __eq__(self, other):
        return self.my_item == other.my_item


print(12 == 12)
print(12 == 1)
print(12 != 5)
print('spam' == 'spam')
print('spam' == 'spam ')
print('spam' != 'spam ')
print(12 == '12')

a = Foo(5)
b = Foo(5)
print(a == b)
print(a != b)
print(a is b)
