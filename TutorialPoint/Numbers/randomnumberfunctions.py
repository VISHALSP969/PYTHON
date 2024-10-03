import random

# choice()
list1 = [1, 2, 3, 4, 5]
random_choice = random.choice(list1)
print(random_choice)

tuple1 = [1, 2, 3, 4, 5]
random_choice = random.choice(tuple1)
print(random_choice)

set1 = [1, 2, 3, 4, 5]
random_choice = random.choice(set1)
print(random_choice)
print('------------')

# randrange()
print(random.randrange(0, 100))
print(random.randrange(1, 20, 5))
print(random.randrange(2, 3))
print('------------')

# random()
print(random.random())
print(random.random() * 10)
print(random.random() * 100)
print('------------')

# seed()
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

random.seed(10)
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

random.seed(5)
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

random.seed(10)
print(random.randint(1, 10))
random.seed(10)
print(random.randint(1, 10))
random.seed(10)
print(random.randint(1, 10))

random.seed()  # uses system time as seed value
print(random.randint(1, 10))
print('------------')

# shuffle()
list1 = [1, 2, 3, 4, 5]
print(list1)
random.shuffle(list1)
print(list1)
print('------------')
