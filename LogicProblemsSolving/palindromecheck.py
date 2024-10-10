# print('Palindrome check')
# num = int(input('Enter a number : '))
# num1 = num
# sum = 0
# while num1:
#     r = num1 % 10
#     sum = sum * 10 + r
#     num1 //= 10
#
# if num == sum:
#     print('Palindrome number')
# else:
#     print('Not a palindrome number')


print('Palindrome check')


def is_palindrome(s):
    return s == s[::-1]


s = input('Enter yor input : ')
if is_palindrome(s):
    print('Your input is palindrome')
else:
    print('Your input is not palindrome')
