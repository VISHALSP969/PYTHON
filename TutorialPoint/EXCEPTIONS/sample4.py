try:
    result = 10 / 0
except(ZeroDivisionError, ValueError):
    print('Either division by zero  or a value error occurred.')

try:
    num = int(input('Enter a number :'))
    result = 10 / num
except (ZeroDivisionError, ValueError):
    print('Either you entered a non-integer value or tried to divide by zero.')

try:
    num = int(input('Enter a number :'))
    result = 10 / num
except ZeroDivisionError:
    print('Error: You cannot divide by zero')
except ValueError:
    print('Error:Invalid input.Please enter an integer')

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")
