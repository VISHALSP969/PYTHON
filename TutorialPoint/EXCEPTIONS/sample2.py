try:
    fo = open('testfile.txt', 'r')
    fo.write('This is my test file for exception handling!')
except IOError:
    print('Error: can\'t find file or read data')
else:
    print('Written the content successfully')
