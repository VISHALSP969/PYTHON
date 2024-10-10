# print('Sum of Digits')
# num = int(input('Enter the number : '))
#
# num1 = num
# digit_sum = 0
#
# while num1:
#     digit_sum+=(num1%10)
#     num1//=10
#
# print(f'Sum of digits of number {num} is {digit_sum}')

print('Sum of digits')


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


print(sum_of_digits(123))
print(sum_of_digits(4567))
