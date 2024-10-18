# using the range() function
for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

# using range() function to make a list of numbers
numbers = []
for value in range(1, 6):
    numbers.append(value)
print(numbers)

numbers = list(range(1, 6))
print(numbers)

# list of even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# list of squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
