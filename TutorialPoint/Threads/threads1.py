import threading


# function to be executed in a separate thread
def print_numbers():
    for i in range(5):
        print(i)


# create a thread
thread = threading.Thread(target=print_numbers)

# start the thread
thread.start()

print('Main thread continues to run in parallel')
