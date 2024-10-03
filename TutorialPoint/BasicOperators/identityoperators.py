a = 20
b = 20

if a is b:
    print('a and b have same identity')
else:
    print('a and b do not have same identity')

print(id(a))
print(id(b))

c = 10
d = 20

if c is d:
    print('c and d have same identity')
else:
    print('c and d do not have same identity')

print(id(c))
print(id(d))

