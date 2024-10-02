# while True:
#     for i in range(1, 5):
#         if i == 2:
#             break       # only break out of inner loop

# def break_loop():
#     for i in range(1, 5):
#         if i == 2:
#             return (i)
#         print(i)
#     return 5
#
#
# x = break_loop()
# print(x)


def break_all():
    for j in range(1, 5):
        for i in range(1, 4):
            if i * j == 6:
                return i
            print(i * j)


x = break_all()
print(x)
