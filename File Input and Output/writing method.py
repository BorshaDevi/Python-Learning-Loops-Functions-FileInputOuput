# First,open the file  before writing to it.
# There are 2 types of writing modes . 

# 1.w 
# [It means,this mode  overwrites the entire file. It removes all existing data and then writes  new data.].
# w clears the file at open time, not at write time.
# After the file is opened in w mode, calling write() multiple times does not remove previous writes;
# instead, each write() appends data from the current file pointer position.

#  2.a 
# [It means, this mode  adds  new data to the end of the entire file. 
# It does not remove existing data,It simply appends new data.]

# a
file=open('F:\\Drive D\\Python3\\file.texts\\filetexts.txt','a')
file.write('This is write for add some text in the file after the end text.')
file.write('\nI want to learn write method , thats why I write this')  
file.close()                     
#  w
file1=open('F:\\Drive D\\Python3\\file.texts\\filetexts.txt','w')
file1.write('Now I want to learn about SQL')
file1.write('Because I want to be a Data Analyst')
file1.write ("\n I learn about PowerBI for data vi")
file1.write('\n then I learn python library Punda, Numpy')
file1.write('\n I learn about more data analytics')
file.close()
