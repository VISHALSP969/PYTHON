# string concatenation
str1 = "Hello"
str2 = "World"
print(str1 + str2)

# string repetition
print(str1 * 3)

# slice
print(str1[0])
print(str1[1])

# range slice
print(str1[2:4])

# membership
if 'H' in str1:
    print("H present in str1")

if 'B' not in str1:
    print("B not present in str1")

# format
num = 10
print("number is %d" % (num))
