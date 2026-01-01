# Loops are used to repeat instructions.
# While and For  .There are two types of loops.


# While 
# A while loop repeatedly executes a block of code as long as the condition is true.
# Once the condition becomes False, the loop stops.
count=1
while count <=5:
           print('hello')
           count +=1
# hello
# hello
# hello
# hello
# hello

# Here count variable is a iterator.
# And Running in the loop that is called iteration.  1 iteration means 1 loop completed.
i=10
while i>=1:
        print(i)
        i -=1

# keyword : =
# break :used to terminate the loop when encountered.

i=1
while i<= 5:
    print(i)
    if(i==3):
        break
    i +=1
print('end loop')

list2=(1,4,9,16,25,36,49,64,81,100,36)
x=36
i=0
# 1  
while i<=len(list2)-1:
    if(list2[i]==x):
        print('Found')
        break
    else:
        print('Not Found')
    i +=1
print('End Loop')   

# 2
while i<=len(list2)-1:
    if(list2[i]==x):
        print('Found')
    else:
        print('Not Found')
    i +=1
print('End Loop')    

# Now the question is what is the different between this 2 codes?

# In 1st one - when the value x found,the break statement stop the loop immediately.
# So,the loop does not continue searching after finding the value.

# In 2nd one - when the value x found,the loop continues running because there is a no break statement.
# That is why it checks all elements and can find the value again.


# Continue :continue skips the current iteration and moves to the next iteration of the loop.

i=0
while i<=5:
    if(i==3):
        i +=1
        continue
    print(i)
    i += 1
# 0
# 1
# 2
# 4
# 5
#when i==3 is true it increases the value by 1 and then continue skip the print statement and starts the next iteration.
# so,3 is not print.


# If we need to print only odd numbers.
i=1
while i<=10:
    if(i%2==0):
        i +=1
        continue
    print(i)
    i+=1
# If we need to print only even numbers.
i=1
while i<=10:
    if(i%2!=0):
        i +=1
        continue
    print(i)
    i+=1
