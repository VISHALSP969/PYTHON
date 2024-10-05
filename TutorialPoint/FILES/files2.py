# open a file
fo = open('foo.txt', 'wb')
print('Name of the file :', fo.name)
print('Closed or not :',fo.closed)

# close opened file
fo.close()
print('Closed or not :',fo.closed)
