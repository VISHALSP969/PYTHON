for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(5):
    print(i)

for i in range(0, 5):
    print(i)

# Iterate over lists
for x in ['one', 'two', 'three', 'four']:
    print(x)

for x in range(1, 6):
    print(x)

for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)

x = map(lambda e: e.upper(), ['one', 'two', 'three', 'four'])
print(list(x))

# Loops with an 'else' clause
for i in range(3):
    print(i)
else:
    print('Done')

# break statement
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Done")

for x in [1, 2, 'apple', True, 2.34]:
    if type(x) is not int:
        print(x)
        break
else:
    print("no exception")

# pass statement
for x in range(10):
    pass


# Iteration over dictinaries
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)

for key in d.keys():
    print(key)

for values in d.values():
    print(values)

for key,item in d.items():
    print(key,'::',item)