# open a file
fo = open('new.txt', 'r+')
print('Name of the file :', fo.name)

# fid = fo.fileno()
# print('fid :', fid)

# here it does nothing,but you can call it with read operation
# fo.flush()

# ret = fo.isatty()
# print('Return value :', ret)

# for index in range(5):
#     line=fo.next()
#     print('Line no : %d - %s'%(index,line))
# for index, line in enumerate(fo):
#     print('Line no: %d - %s' % (index, line))

# read file
# line=fo.read(10)
# print(line)

# read one complete line
# line = fo.readline()
# print(line)
# # tells current position
# print(fo.tell())
# # reads only 5 characters
# line = fo.readline(5)
# print(line)
# # tells current position
# print(fo.tell())

# again set pointer to the beginning
# set pointer from beginning
# fo.seek(0,0)
# line = fo.readline()
# print(line)

# line = fo.readline()
# print(line)
# # Now truncate remaining file
# fo.truncate()
# line = fo.readline()
# print(line)

# str1 = '\nThis is 6th line\n'
# # pointing pointer to file end
# fo.seek(0, 2)
# print(fo.tell())
# fo.write(str1)

seq = ['This is 7th line\n', 'This is 8th line\n']
fo.seek(0,2)
fo.writelines(seq)

# close opened file
fo.close()
