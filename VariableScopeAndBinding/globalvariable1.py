x = 10
print("x =", x)


def modify_global():
    # global x
    x = 100


modify_global()
print("x =", x)
