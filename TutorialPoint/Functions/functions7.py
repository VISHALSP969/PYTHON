# default argument - argument that assumes a default value if a value is not
# provided in the function call for that argument

def printinfo(name, age=25):
    print(name, age)
    return


printinfo(name='John', age=22)
printinfo(name='Zara')
