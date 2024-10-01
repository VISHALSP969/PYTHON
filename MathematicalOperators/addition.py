import operator

a, b = 1, 2

print(a + b)
a += b
print(a)

a = operator.add(1, 2)
print(a)

print(10 + 20)
print(10.0 + 20)
print(10 + 20.0)
print(10.0 + 20.0)
print(10 + (20 + 5j))
print((3 + 2j) + (5 + 10j))

# in case of strings + acts for concatenation
print("first string" + "second string")

print([1, 2, 3] + [4, 5, 6])
print((1, 2, 3) + (4, 5, 6))

