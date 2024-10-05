# required arguments- args passes in correct positional order and number of args should match

def printme(str1):
    print(str1)
    return


# printme()   # TypeError
# printme("")
printme('sample string')
