filename='guest.txt'

with open(filename,'a') as file_object:
    while True:
        name=input("Enter the name (Enter q for exit) : ")
        if name=='q':
            break
        file_object.write(name+"\n")