# open the file
fo=open('foo.txt','r+')
str=fo.read(6)
print(str)

# close opened file
fo.close()