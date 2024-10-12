def reverse_string(s):
    rev = s[::-1]
    return rev


str_input = input('Enter a string : ')

reversed_string = reverse_string(str_input)
print(reversed_string)
