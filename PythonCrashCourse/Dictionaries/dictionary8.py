person = {'first_name': 'john', 'last_name': 'doe', 'age': 28, 'city': 'california'}
for key, value in person.items():
    print("key:", key, "  value:", value)

rivers = {'the amazon': 'brazil', 'nile': 'egypt', 'the ganges': 'india', 'the mississippi': 'usa',
          'the thames': 'england'}
for river, country in rivers.items():
    print(river.title() + " runs through " + country.upper())

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.upper())

favorite_languages={'jenny':'c','mosh':'java','tim':'python','akshay':'javascript','jenny':'python'}
print(favorite_languages)
names=['jenny','edward','akshay']
for name in names:
    if name in favorite_languages.keys():
        print(name.title()+",thanks for taking the poll.")
    else:
        print(name.title()+",please take the poll.")
