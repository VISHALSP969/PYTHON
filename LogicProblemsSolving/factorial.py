num = int(input('Enter a number : '))


def factorial(n):
    if n > 1:
        fact = 1
        while n:
            fact *= n
            n -= 1
        return fact
    elif n == 0 or n == 1:
        return 1
    else:
        return 'No factorial'


result = factorial(num)
print(result)
