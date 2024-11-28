filename='responses.txt'

with open(filename,'a') as file_object:
    while True:
        response=input("Why you like programming?('q' for exit) : ")
        if response=='q':
            break
        file_object.write(response+'\n')