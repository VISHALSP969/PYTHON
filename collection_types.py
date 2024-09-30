# Collection Types

from collections import defaultdict

# Python Lists
int_list = [1, 2, 3]
print(int_list)
string_list = ['abc', 'defghi']
print(string_list)

empty_list = []  # empty list
print(empty_list)

mixed_list = [1, 'abc', True, 2.34, None]  # mixed types are possible within the lis
print(mixed_list)

nested_list = [['a', 'b', 'c'], [1, 2, 3]]  # Nested list
print(nested_list)

names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']  # list items are indexed
print(names[0])  # index of first item is 0
print(names[2])
print(names[-1])  # negative index starts from the end
print(names[-2])

names[0] = 'Ann'  # lists are mutable
print(names)

names.append('Sia')  # add item at the end of the list
print(names)

names.insert(1, 'Nikki')  # add items at specified index
print(names)

names.remove('Bob')  # remove the first occurrence specified item
print(names)

print(names.index('Ann'))  # gives index of specified item

print(len(names))  # gives count of list items

print(names.count('Ann'))  # give count of specified item

names.reverse()  # reverse the order of list,return None
print(names)

print(names.pop())  # remove and returns last item
print(names)

for element in names:
    print(element)

# Python Tuples
one_member_tuple = ('only member',)
print(one_member_tuple)
one_member_tuple = 'only_member',
print(one_member_tuple)
one_member_tuple = tuple(['one member'])
print(one_member_tuple)

# Python Dictionaries
state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanat'
}
print(state_capitals)
print(state_capitals['California'])
keys = state_capitals.keys()
print(keys)
values = state_capitals.values()
print(values)

for x in keys:
    print(state_capitals[x])

#print(state_capitals['Alabama'])        #key error

# Python Sets
first_names = {'Adam', 'Beth', 'Charlie'}
print(first_names)

my_list = [1, 2, 3]
my_set = set(my_list)
print(my_set)

# defaultdict
state_capitals=defaultdict(lambda:'Boston')
print(state_capitals['Alabama'])
