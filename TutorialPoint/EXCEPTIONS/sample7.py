# def functionName(level):
#     if level<1:
#         raise 'Invalid level'(level)

try:
    raise ValueError('Custom error message',404)
except ValueError as e:
    print(f'Error : {e}')
    print(f'Error args : {e.args}')
