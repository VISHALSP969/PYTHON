dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print(dimensions)

# dimensions[0]=250       # Type Error

# looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

# writing over a tuple
dimensions = (400, 100)
print("Modified dimensions : ")
for dimension in dimensions:
    print(dimension)
