
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


