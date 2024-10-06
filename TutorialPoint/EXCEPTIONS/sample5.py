# try:
#     fo=open('testfile.txt','w')
#     fo.write('This is my test file for exception handling')
# finally:
#     print('Error: can\'t find file or read data')


try:
    fo=open('testfile.txt','w')
    try:
        fo.write('This is my test file for exception handling!!!!')
    finally:
        print('Going to close  the file')
        fo.close()
except IOError:
    print('Error: can\'t find file or read data')