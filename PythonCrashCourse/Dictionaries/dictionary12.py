# make an empty list to store people in
people = []

# define some people ,an add them to the list
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka'
}
people.append(person)

person = {
    'first_name': 'lemmy',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitka'
}
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 11,
    'city': 'sitka',
}
people.append(person)

# display all the information in the dictionary
print(people)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    print(f"{name} , of {city}, is {age} years old.")

print("\n-------------------------------------------\n")

# make an empty lis to store the pets in
pets = []

# make individual pets, and store each one in the list
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs'
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds'
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes'
}
pets.append(pet)

# display information about each pet
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key} : {value}")

print("\n-------------------------------------------\n")

favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt.verstovia', 'the play ground', 'new hampshire']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places: ")
    for place in places:
        print(f"-{place.title()}")

print("\n-------------------------------------------\n")

favorite_numbers = {
    'mandy': [42, 7],
    'mican': [42, 39, 56],
    'gus': [7, 12]
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"    {number}")

print("\n-------------------------------------------\n")

cities = {
    'santiago': {
        'country': 'chile',
        'population': 6310000,
        'near by mountains': 'andes'
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'near by mountains': 'alaska range'
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975453,
        'near by mountains': 'himalaya'
    }
}

for city, cityinfo in cities.items():
    country = cityinfo['country'].title()
    population = cityinfo['population']
    mountains = cityinfo['near by mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mounats are nearby.")
