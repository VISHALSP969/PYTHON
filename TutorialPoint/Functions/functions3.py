# pass by value
def changeme(mylist):
    mylist = [1, 2, 3, 4]
    print(id(mylist))
    print('Values inside the function :', mylist)
    return


mylist = [10, 20, 30, 40]
changeme(mylist)
print(id(mylist))
print('Values outside the function :', mylist)
