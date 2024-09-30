# Datatypes

# boolean
x = True
print(type(x))
y = False
print(x and y)
print(x or y)
print(not x)

print(issubclass(bool, int))
print(isinstance(True, bool))

# Numbers
# integers
a = 2
print(type(a))
print(a)
b = 987654321987654321
print(b)
# float
a = 2.0
print(type(a))
print(a)
b = 100e0
print(b)
c = 123456789e1
print(c)
# complex
a = 2 + 3j
print(type(a))
print(a)
b = 100 + 10j
print(b)

# strings
a = 'hello'
print(a)
print(type(a))
b = b'hello'
print(b)

# tuple
a = (1, 2, 3, 1, 2)
print(a)
print(type(a))
print(type(a))
b = ('a', 1, 'python', (1, 2))
print(b)
# b[2]='something else'     #Type error

# list
a = [1, 2, 3, 1, 2]
print(a)
print(type(a))
b = ['a', 1, 'python', (1, 2), [1, 2]]
print(b)
b[2] = 'something else'
print(b)

# set
a = {1, 2, 'a', 1, 2}
print(a)
print(type(a))

# dict
a = {1: 'one', 2: 'two'}
print(a)
print(type(a))
b = {'a': [1, 2, 3], 'b': 'a string'}
print(b)

a = None
print(a)
print(type(a))

# Converting between datatypes
a = '123'
print(a)
b = int(a)
print(b)

a = '123.456'
b = float(a)
# c = int(a)        #value error:invalid literal for int()
d = int(b)
print(a)
print(b)
print(d)

a = 'hello'
b = list(a)
print(b)
c = set(a)
print(c)
d = tuple(a)
print(d)

x=[1,2,3]
def fn(x):
    x.append(4)
fn(x)
print(x)

