# Defining a class
class Dog:
    # constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # class methods
    def sit(self):
        print(self.name.title()+' is now sitting.')

    def roll_over(self):
        print(self.name.title()+" rolled over!")

# creating instance of class
my_dog=Dog('willie',6)
# accessing class attributes
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
# accessing class methods
my_dog.sit()
my_dog.roll_over()

your_dog=Dog('lucy',3)
print("My dog's name is "+your_dog.name.title()+".")
print("My dog is "+str(your_dog.age)+" years old.")
your_dog.sit()
your_dog.roll_over()