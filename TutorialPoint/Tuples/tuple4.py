tuple1=(1,2,3,4,5)
tuple2=(6,7)

# length
print(len(tuple1))

# concatenation
print(tuple1+tuple2)

# repetition
print(("Hi",)*4)

# membership
print(3 in tuple1)
print(7 not in tuple1)

# iteration
for x in tuple1:
    print(x)
