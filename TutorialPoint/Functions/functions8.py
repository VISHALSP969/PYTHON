# variable length arguments - need to process a function for more arguments than you specified while
# defining the function

def printinfo(arg1, *vartuple):
    print('Output is : ')
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfo(10)
printinfo(70, 60, 50)
