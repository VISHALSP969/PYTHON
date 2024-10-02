from array import array

my_array = array('i', [1, 2, 3, 4, 5])
print(type(my_array))
print(my_array)

print(my_array[0])
print(my_array[1])
print(my_array[2])

for i in my_array:
    print(i)

# append any value to the array
my_array.append(6)
print(my_array)

# insert value in an array
my_array.insert(0, 0)
print(my_array)
my_array.insert(7, 7)
print(my_array)

# extend python array
my_array_extend = array('i', [8, 9, 10])
my_array.extend(my_array_extend)
print(my_array)

#  add items from list using fromlist()
my_array = array('i', [1, 2, 3, 4, 5])
c = [6, 7, 8]
my_array.fromlist(c)
print(my_array)

# remove()
my_array.remove(7)
print(my_array)

# pop()
my_array.pop()
print(my_array)

my_array = array('i', [1, 2, 3, 4, 5])
print(my_array[0])
print(my_array[1])
print(my_array[2])
print(my_array[3])
print(my_array[4])

# reverse()
my_array.reverse()
print(my_array)

print(my_array.buffer_info())

# count()
print((my_array.count(5)))
print(my_array.count(7))

# tostring()
# my_char_array = array('c', ['g', 'e', 'e', 'k'])
# str1 = my_char_array.tostring()
# print(str1)

my_array = array('i', [1, 2, 3, 4, 5])
c = my_array.tolist()
print(c)

# my_char_array=array('c',['g','e','e','k'])
# my_char_array.fromstring("stuff")
# print(my_char_array)
