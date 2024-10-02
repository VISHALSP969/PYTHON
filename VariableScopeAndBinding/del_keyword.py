x = 5
print(x)
del x


# print(x)      # Name Error


class A:
    pass


a = A()
a.x = 7
print(a.x)
del a.x
# print(a.x)    #Attribute error

x = {'a': 1, 'b': 2}
print(x)
print(x['a'])
print(x['b'])
del x['a']
print(x)
# print(x['a'])     # Key error

x = [0, 1, 2, 3, 4, 5]
print(x)
print(x[2])
del (x[1:3])
print(x)
print(x[2])
