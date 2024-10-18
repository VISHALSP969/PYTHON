for num in range(1, 21):
    print(num)
print("\n")

for value in range(1, 1000001):
    print(value)
print("\n");

numbers = []
for value in range(1, 1000001):
    numbers.append(value)
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print("\n")

odd_numbers = list(range(1, 20, 2))
for value in odd_numbers:
    print(value)
print("\n")

cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
for value in cubes:
    print(value)
print("\n")

cubes = [value ** 3 for value in range(1, 11)]
for value in cubes:
    print(value)
print("\n")
