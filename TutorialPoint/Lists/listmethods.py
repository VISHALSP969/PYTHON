list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# compare
print(list1 == list2)
print(list1 != list2)
# print(cmp(list1,list2))       # Name Error

# len() function
print(len(list1))

# max() function
print(max(list1))

# min() function
print(min(list1))

# list() method
tuple1 = (1, 2, 3)
l = list(tuple1)
print(l)
print('------------')

# list methods
# append()
list1 = [1, 2, 3]
print(list1)
list1.append(4)
print(list1)
list1.append(5)
print(list1)

# count()
list1 = [1, 2, 3, 1, 2, 4, 5]
print(list1.count(5))
print(list1.count(1))

# extend()
list1 = [1, 2, 3]
list2 = [4, 5]
tuple1 = (6, 7, 8, 9, 10)
print(list1)
list1.extend(list2)
print(list1)
list1.extend(tuple1)
print(list1)

# index()
list1 = [1, 2, 3, 4, 5]
print(list1.index(2))
print(list1.index(4))

# insert()
list1 = [1, 2, 3, 4, 5]
print(list1)
list1.insert(2, 7)
print(list1)
list1.insert(5, 8)
print(list1)

# pop()
list1 = [1, 2, 3, 4, 5]
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)

# remove()
list1 = [1, 2, 3, 4, 5]
print(list1.remove(5))
print(list1)
list1.remove(2)
print(list1)

# reverse()
list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1.reverse())
print(list1)

# sort()
list1 = [7, 3, 9, 4, 1, 5]
print(list1.sort())
print(list1)


