places = ['Madrid', 'Melbourne', 'Lisbon', 'Paris', 'London']
print(places)

print(sorted(places))
print(places)

print(sorted(places, reverse=True))
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places = ['Madrid', 'Melbourne', 'Lisbon', 'Paris', 'London']
print(places)
places.sort(reverse=True)
print(places)

print("Items in list :", len(places))

my_list = ["Everest", "Madrid", "Amazon", "New york", "London", "Maldives","Mount K2","Paris"]
print(sorted(my_list))
print(sorted(my_list,reverse=True))
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

my_list = ["Everest", "Madrid", "Amazon", "New york", "London", "Maldives","Mount K2","Paris","Amsterdam"]
my_list.reverse()
print(my_list)

print(len(my_list))

my_list = ["Everest", "Madrid", "Amazon", "New york", "London", "Maldives","Mount K2","Paris","Amsterdam","Tokyo"]
my_list.append("Melbourne")
print(my_list)

del my_list[6]
print(my_list)

my_list.remove("Amsterdam")
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(2)
print(my_list)

my_list.insert(3,"Moscow")
print(my_list)
