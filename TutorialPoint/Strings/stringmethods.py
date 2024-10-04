str1 = "Hello World"
# string case methods
print(str1.upper())
print(str1.lower())
print(str1.swapcase())

str1 = "hello world"
print(str1.capitalize())
print(str1.title())

# string search methods
print(str1.find('world'))
print(str1.find("WORLD"))

print(str1.index('world'))
# print(str1.index('WORLD'))    # Value Error

str1 = "Hello world world"
print(str1.rfind('world'))

print(str1.startswith("Hello"))
print(str1.startswith('hello'))

print(str1.endswith('world'))
print(str1.endswith('hello'))

# string modification methods
str1 = "Hello world"
print(str1.replace('world', 'Python'))

str1 = "     Helloooo     "
print(str1)
print(str1.strip())
print(str1.rstrip())
print(str1.lstrip())

# split method
str1 = "Hello world world"
print(str1.split())
print(str1.rsplit())

str1 = "Hello,world,world world"
print(str1.split(','))

# join method
words = ['hello', 'world']
print(" ".join(words))
words = ['hello', 'world', 'world']
print("".join(words))
print(" ".join(words))

# stricg check methods
s = "hello"
print(s.isalpha())
print(s.isdigit())
print(s.isnumeric())
s = "12345"
print(s.isalpha())
print(s.isdigit())
print(s.isnumeric())

s = "abc123"
print(s.isalnum())

s = "    "
print(s.isspace())

s = "hello"
print(s.islower())
print(s.isupper())

s = "HELLO"
print(s.isupper())
print(s.islower())

s = "Hello World"
print(s.istitle())
s = "hello world"
print(s.istitle())

# length method
s = "helloo world"
print(len(s))

# count method
print(s.count('o'))
print(s.count('l'))
print(s.count('b'))

# string alignment methods
s = "center"
print(s.center(20))
print(s.ljust(20))
print(s.rjust(20))

# encoding and decoding
s = "hello"
encoded_s = s.encode('utf-8')
print(encoded_s)

decoded_s = encoded_s.decode('utf-8')
print(decoded_s)

# other methods
s = "45"
print(s.zfill(5))

s = "hello world"
print(s.partition(" "))
print(s.partition("o"))
