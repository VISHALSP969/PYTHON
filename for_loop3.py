# sum of all odd numbers and even numbers upto a limit
number=int(input("Enter a number : "))
even=0
odd=0
for i in range(number):
    if i%2==0:
        even+=i
    else:
        odd+=i
print(f"Sum of Even numbers are {even} and Odd numbers are {odd}")
