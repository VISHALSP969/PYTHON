# int() function
float_to_int=int(3.5)
print(float_to_int)
string_to_int=int("123")
print(string_to_int)

number=input("Enter a number : ")
print(type(number))
number=int(input("Enter a number : "))
print(type(number))

# float() function
int_to_float=float(4)
print(int_to_float)
string_to_float=float("25")
print(string_to_float)

# str() function
int_to_string=str(8)
print(int_to_string)
float_to_string=str(3.5)
print(float_to_string)

# chr() function
ascii_to_char=chr(100)
print(ascii_to_char)

# complex() function
complex_with_string=complex("1")
print(complex_with_string)
complex_with_number=complex(5,8)
print(complex_with_number)

# ord() function - returns an integer represent the unicode character
unicode_for_integer=ord('4')
print(unicode_for_integer)
unicode_for_alphabet=ord("Z")
print(unicode_for_alphabet)
unicode_for_character=ord("#")
print(unicode_for_character)

# hex() function
int_to_hex=hex(255)
print(int_to_hex)

# oct() function
int_to_oct=oct(255)
print(int_to_oct)