import threading


# function that takes arguments
def greet(name):
    print(f'Hello {name}')


# create and start thread with arguments
thread = threading.Thread(target=greet, args=('Alice',))

thread.start()
thread.join()

print('Main thread waits until the worker thread is done')
