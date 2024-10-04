name = 'Alice'
age = 30

print("%s is %d years old" % (name, age))

pi = 3.14
print("Value of pi is %.2f" % pi)

# str.format()
print("{} is {} years old".format(name, age))
print("Value of pi is {}".format(pi))

print("{0} is {1} years old".format(name, age))

print("{name} is {age} years old".format(name="John", age=35))

print("Value of pi is {:.2f}".format(pi))

# f-strings
formatted_string = f"My name is {name}, and Iam {age} years old."
print(formatted_string)

formatted_string = f"Nex year, I will be {age + 1} years old"
print(formatted_string)

print(f"The value of pi is {pi:.2f}")

val = 42.5
print(f"Value={val:.0f}")
print(f"Value={val:.2f}")

# padding alignment
print(f"{'left':<10} {'center':^10} {'right':>10}")
