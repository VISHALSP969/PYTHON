def outer():
    x=5
    print("x =",x)
    def inner():
        nonlocal x
        x=50

    inner()
    print("x =",x)

outer()