name="John Doe"
print(name)

# str.format()
# positional argument
country=input("Which country do you live in? ")
print("I live in {0}.".format(country))

a=10
b=20
print("The value of a is {0} and b is {1}.".format(a,b))
print("The value of b is {1} and a is {0}.".format(a,b))

# keyword argument
print("Give me {ball} ball.".format(ball="tennis"))

# f-strings
country=input("Which country do you live in? ")
print(f"I lived in {country}")
