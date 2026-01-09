# read():

# In the read method ,we can pass parameter. 
file=open('F:\\Drive D\\Python3\\file.texts\\filetexts.txt','r')
para=file.read(5)   # 5 means give me first 5 letter.
print(para)
file.close()

# readline():

file=open('F:\\Drive D\\Python3\\file.texts\\filetexts.txt')
line1=file.readline()  
 #Hello .[it is from my file text]  After this you can see a space because when we read this line, 
 # it also includes the \n character,which represent a newline.We cannot see it,
 # but it comes with readline().
print(line1)
file.close()

file=open('F:\\Drive D\\Python3\\file.texts\\filetexts.txt')
line1=file.readline()
line2=file.readline()
print(line1)
print(line2)
file.close()

# readlines()
file=open('F:\\Drive D\\Python3\\file.texts\\filetexts.txt')
line=file.readlines()
print(line)
file.close()


file=open('F:\\Drive D\\Python3\\file.texts\\filetexts.txt')
li=file.read()
print(li)
# here all the text is printed first. 
# After that,readline() cannot read anything.
# This happens because the file works like a pointer.
# Once read() reads  the entire file,the pointer moves to the end.
# So when we try to read line by line , nothing is found because everything has already been read.
line1=file.readline()
print(line1)
line2=file.readline()
print(line2)

file.close()