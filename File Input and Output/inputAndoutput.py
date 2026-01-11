# We have to open a file before reading or writing.


# Syntax: variable=open(“file_name”, “mode”)  
# data=variable.read()   [read is an operation.]
# variable.close() # Must close the file.

file=open('F:\\Drive D\\Python3\\file.texts\\filetexts.txt')
da=file.read()
print(da)
file.close()

file=open('F:\\Drive D\\Python3\\file.texts\\filetexts.txt','r')
da=file.read()
print(da)
file.close()


# With keyword

# with open(‘file name’,mode) as fi:
#     fi.read/write()
# fi means fi=open(‘file name’,mode)

#  we use with,so there is no need to call file.close() , because with automatically closes the file.

# " with " keyword  can be used for  all types of operation.

with open('sample.txt','r') as f:
    re=f.read()
    print(re)

with open('sample.txt','w')  as f:
    f.write('Learn about with.')  



