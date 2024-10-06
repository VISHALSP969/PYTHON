# try:
#     result=10/0
# except ZeroDivisionError as e:
#     print(f'Exception occurred {e}')


# try:
#     num=int(input('Enter a number : '))
#     result=10/num
# except ValueError as e:
#     print(f'Error : {e}')
# except ZeroDivisionError as e:
#     print(f'Error : {e}')

try:
    res=10/0
except ZeroDivisionError as e:
    print(f'Error : {e}')
    print(f'Error args : {e.args}')
