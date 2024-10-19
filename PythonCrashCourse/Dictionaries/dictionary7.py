# looping through all key value pairs

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}

for key, value in user_0.items():
    print('key : ' + key)
    print('value : ' + value)

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

# looping through all keys
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ",I see your favorite language is " + favorite_languages[name].title())

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

# looping through dictionary keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title()+",thank you for taking the poll.")

# looping through all values in a dictionary
for language in favorite_languages.values():
    print(language.title())

print('------------')
for language in set(favorite_languages.values()):
    print(language)
