def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print('Arguments passed:', args, kwargs)
        return func(*args, **kwargs)

    return wrapper


@decorator_with_args
def add(a, b):
    return a + b


print(add(5, 10))
