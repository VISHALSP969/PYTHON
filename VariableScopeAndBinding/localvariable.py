def foo():
    a = 5
    print(a)


def foo1():
    if True:
        b = 5
    print(b)


def foo2():
    if False:
        c = 5
    # print(c)      # UnboundLocalError


foo()
# print(a)      # Name Error
foo1()
foo2()
