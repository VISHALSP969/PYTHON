motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modifying elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to a list
motorcycles.append("honda")  # append element to the end of list
print(motorcycles)
motorcycles.append("bajaj")
print(motorcycles)

# insert elements to a list
motorcycles = ['ducati', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, "honda")
print(motorcycles)
motorcycles.insert(4, "bajaj")
print(motorcycles)

# removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]  # delete elements using del keyword
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# remove an item using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

# removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'bajaj', 'royal enfield', 'Hero', 'ducati']
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
