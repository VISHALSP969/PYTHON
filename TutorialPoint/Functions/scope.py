total = 0  # This is global variable


def sum(arg1, arg2):
    total = arg1 + arg2  # here total is local variable
    print('Inside the function local total :', total)
    return total


sum(10, 20)
print('Outside the function global total :',total)
