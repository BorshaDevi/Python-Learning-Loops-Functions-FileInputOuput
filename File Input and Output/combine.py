
# r+ = read + overwrite (pointer start) - no truncate

# w+=read + overwrite(There is no pointer position,because the file is truncated.
# There is  no existing content. So do not write any texts then how can it find the pointer position.) - truncate

# a+=read+ append (pointer end) - no truncate.

# Note: truncate means the file becomes empty when it is opened .


# r+ 
file=open('sample.txt','r+')
file.write('It is very interesting.')
print(file.read())  
# Here the pointer writes "It is very interesting " and then moves to the position after 'interesting'.
# so the pointer starts reading from this position.
file.close()

# w+
file=open('sample1.txt','w+')
re=file.read()
print(re) # here we do not find any text. Because it is truncated.
file.write('Add new text') # now write and see in the file. this  text was added.
file.close()

# a+
file=open('sample2.txt','a+')
                                                                                                                                                                   

