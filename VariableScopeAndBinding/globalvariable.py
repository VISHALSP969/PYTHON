x = 'Hi'


def read_x():
    print(x)


read_x()


def read_y():
    y = "Hey"
    print(y)


read_y()

# def read_x_local_fail():
#     if False:
#         x = "Hey"
#     print(x)
#
#
# read_x_local_fail()

x = "Hi"


def change_local_x():
    global x
    x = "Bye"
    print(x)


change_local_x()
print(x)
