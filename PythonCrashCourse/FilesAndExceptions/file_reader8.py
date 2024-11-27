filename='sample.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

    for line in lines:
        new_line=line.replace('sample','demo')
        print(new_line.strip())