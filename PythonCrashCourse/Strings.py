str1 = "This is a string"
print(str1)

str2 = 'This is also a string'
print(str2)

# Changing case in a string with methods
name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())

# Combining or concatenating strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

# Adding whitespace to strings with tabs or newlines
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping whitespaces
favorite_language = 'Python      '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)
favorite_language = favorite_language.rstrip()  # for permanent stripping
print(favorite_language)

favorite_language = '      Python'
print(favorite_language)
favorite_language.lstrip()
print(favorite_language)
favorite_language = favorite_language.lstrip()  # for permanent stripping
print(favorite_language)

favorite_language = '      Python      '
print(favorite_language)
favorite_language.strip()
print(favorite_language)
favorite_language = favorite_language.strip()  # for permanent stripping
print(favorite_language)

message = "One of Python's strength is its diverse community."
print(message)
