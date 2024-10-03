tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])

print(tuple1[:])
print(tuple1[0:])
print(tuple1[:5])
print(tuple1[1:4])
print(tuple1[2:5])

mixed_tuple = ('abcd', 786, 2.23, 'john', '70.2')
print(mixed_tuple)

tuple2 = (1, 2, 3)
tuple3 = (4, 5, 6, 7, 8, 9, 10)
print(tuple2 + tuple3)

print(tuple2 * 3)

# tuple2[0]=0     #Type Error:tuple does not support item assignment
# print(tuple2)

list2 = list(tuple2)
list2[0] = 0
tuple2 = tuple(list2)
print(tuple2)
