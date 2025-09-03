score=float(input("Enter your score : "))
if score<0 or score>1:
    print("Wrong Input")
elif score>0.9:
    print("Your Grade is A")
elif score>0.8:
    print("Your Grade is B")
elif score>0.7:
    print("Your Grade is C")
elif score>0.6:
    print("Your Grade is D")
elif score>0.5:
    print("Your Grade is E")
else:
    print("Your Grade is F")

fruit_type=input("Enter the Fruit Type : ")
if fruit_type=="Oranges":
    print("Oranges are $0.59 a pound")
elif fruit_type=="Apples":
    print("Apples are $0.32 a pound")
elif fruit_type=="Bananas":
    print("Bananas are $0.48 a pound")
elif fruit_type=="Cherries":
    print("Cherries are $3.00 a pound")
else:
    print(f"Sorry,we are out of {fruit_type}")