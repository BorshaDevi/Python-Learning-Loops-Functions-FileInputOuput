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


