a = 'Python is fun!'
b = 'Python is fun!'
print(a == b)
print(a is b)

a = [1, 2, 3, 4, 5]
b = a
print(a == b)
print(a is b)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

x = 10
y = 10
print(x == y)
print(x is y)

x = (1, 2, 3, 4)
y = (1, 2, 3, 4)
print(x == y)
print(x is y)

a = 'short'
b = 'short'
c = 5
d = 5
print(a is b)
print(c is d)

a='not so short'
b='not so short'
c=1000
d=1000
print(a is b)
print(c is d)
