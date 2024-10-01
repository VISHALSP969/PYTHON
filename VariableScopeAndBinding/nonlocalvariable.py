def counter():
    num=0
    def incrementer():
        nonlocal num
        num+=1
        return num
    return incrementer

c=counter()
val=c()
print(val)
val=c()
print(val)
val=c()
print(val)