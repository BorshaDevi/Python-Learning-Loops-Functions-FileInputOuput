#  Python has built-in modules to perform common  file operations.
#  A Module(like a code library) is a file written by another programmer that generally has functions we can use.

# check file:

import os
if os.path.isfile('sample.txt'):
    print('This file found') # If it found the file then it print these, otherways nothing print.


# check directory:

import os
if os.path.isdir('Practice'): # directory check means folder check.
    print('It is a directory')
else:
    print( 'It is not a directory')    

# create directory:

import os
os.mkdir('Sample Folder')

# delete file

import os 
os.remove('sample1.txt')

os.removedirs('Sample Folder') # we can also remove folder with use removedirs function from os module.

#  Rename file

import os
os.rename('sample.txt','sample1.txt')
