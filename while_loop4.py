# Find sum of digits in a number
number=int(input("Enter a number : "))
result=0
remainder=0
while number!=0:
    remainder=number%10
    result=result+remainder
    number=int(number/10)
print(f"The sum of all digits is {result}")