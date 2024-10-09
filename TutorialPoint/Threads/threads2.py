import threading


# function to be executed in a seperate thread
def print_numbers():
    for i in range(5):
        print(i)


# create a thread
thread = threading.Thread(target=print_numbers)

# start the thread
thread.start()

# wait for the thread to complete
thread.join()

print('Main thread waits until the worker thread is done')
