x = 100
y = 200
print(globals())
print(locals())


def sample_func():
    a = 10
    b = 20
    c = 30
    print(globals())
    print(locals())


sample_func()
