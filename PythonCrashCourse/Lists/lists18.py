numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("first 3 items are : ", numbers[0:3])

print("# items from middle if the list : ", numbers[3:6])

print("Last 3 items are : ", numbers[-3:])

pizzas = ['Tandoori chicken pizza', 'Paneer tikka pizza', 'Masala pizza', "Keema pizza", "Onion pizza"]
friend_pizzas = pizzas[:]
pizzas.append("California pizza")
friend_pizzas.append("Greek pizza")

print("My favorite pizzas are :", pizzas)
print("My friend's favorite pizzas are :", friend_pizzas)

for food in pizzas:
    print(food)

for food in friend_pizzas:
    print(food)
