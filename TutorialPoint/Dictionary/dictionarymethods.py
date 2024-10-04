# clear()
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)
my_dict.clear()
print(my_dict)

# copy()
my_dict = {"a": 1, "b": 2, "c": 3}
new_dict = my_dict.copy()
print(new_dict)

# get()
my_dict = {"a": 1, "b": 2}
print(my_dict.get('a'))
print(my_dict.get('c'))
print(my_dict.get('c', 'N/A'))

# items()
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.items())

# keys()
print(my_dict.keys())

# values()
print(my_dict.values())

# pop()
print(my_dict.pop('b'))
print(my_dict)

# popitem()
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.popitem())
print(my_dict.popitem())

# update()
my_dict = {"a": 1, "b": 2}
my_dict.update({'c': 3, 'd': 4})
print(my_dict)

# setdefault()
my_dict = {"a": 1}
print(my_dict.setdefault('b', 2))
print(my_dict)
print(my_dict.setdefault('c', 4))
print(my_dict)

# fromkeys()
keys=['a','b','c']
new_dict=dict.fromkeys(keys,0)
print(new_dict)
