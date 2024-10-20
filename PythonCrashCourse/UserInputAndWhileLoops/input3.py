rental_car = input("What kind of car you like?\n")
print("Let me see if I can find you a " + rental_car)

numbers = input("How many members are in your dinner group?\n")
numbers = int(numbers)
if numbers > 8:
    print("Please wait for a while.")
else:
    print("Table is ready!")

number=int(input("Enter a number : "))
if number%10==0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
