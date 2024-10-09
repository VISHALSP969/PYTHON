def add_greeting(func):
    def wrapper():
        print('Hi!')
        func()
        print('Goodbye!')

    return wrapper


@add_greeting
def greet():
    print('How are you?')


greet()
