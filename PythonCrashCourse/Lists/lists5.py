# sorting a list permenantly with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(cars.sort())      # returns None
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(cars.sort())
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list : ")
print(cars)
print("Here is the sorted list : ")
print(sorted(cars))
print("Here is the original list agin : ")
print(cars)

# printing list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
