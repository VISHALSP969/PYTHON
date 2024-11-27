filename='guest_book.txt'

with open(filename,'a') as file_object:
    while True:
        name=input("Enter the name (Type 'q' for exit) : ")
        if name=='q':
            break
        print("Hello "+name+"!")
        file_object.write(name+"\n")