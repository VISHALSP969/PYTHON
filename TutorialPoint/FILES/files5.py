# open a file
fo = open('foo.txt', 'r+')
str1 = fo.read(10)
print('Read string is :', str1)

# check current position
position = fo.tell()
print('Current file position :', position)

# reposition pointer at the beginning once again
position = fo.seek(0, 0)
str2 = fo.read(10)
print('Again read string is :', str2)

# close opened file
fo.close()
