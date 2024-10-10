# print('Prime number check')

# num = int(input('Enter a number : '))
#
#
# def prime_check(n):
#     flag=0
#     for i in range(2, (n // 2) + 1):
#         if n % i == 0:
#             flag=1
#             break
#     if flag==1:
#         print('Not prime')
#     else:
#         print('Prime')
#
#
# prime_check(num)


def is_prime(n):
    if n <= 0:
        return False

    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False

    return True


print(is_prime(17))
print(is_prime(29))
print(is_prime(22))
