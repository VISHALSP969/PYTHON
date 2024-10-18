# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
print("My favorite foods are :", my_foods)
print("My friend's favorite foods are :", friend_foods)

crazy_foods = my_foods[:]
print("My crazy foods :", crazy_foods)

my_foods.append("cannoli")
friend_foods.append('ice cream')

print("My favorite foods are :", my_foods)
print("My friend's favorite foods are :", friend_foods)

crazy_foods = my_foods
print(crazy_foods)
