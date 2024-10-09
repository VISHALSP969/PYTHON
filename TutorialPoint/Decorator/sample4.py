def multiply_decorator(func):
    def wrapper(*args):
        result = func(*args)
        return result * 2

    return wrapper


@multiply_decorator
def add(a, b):
    return a + b


print(add(10, 15))
