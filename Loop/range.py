# Range functions return a sequence of numbers , starting from 0 by default,
# and increments by 1 (by default),and stops before a specified number.


seq=range(5)
for i in seq:
    print(i)

for i in range(10): #range(Stop)
    print(i)    

for i in range(1,8): # range(start,stop)
    print("start and stop",i)      

for i in range(1,12,2):  # range(start, stop ,step)
    print('start , stop and step',i)      


# If I need to print all even number from 1 to 10
for i in range(2,11,2):
    print(i)

# If I need to print all odd number from 1 to 10
for i in range(1,10,2):
    print(i)

# pass
# Pass is a null statement that does nothing.It is used as a placeholder for future code.
#  It means  we have nothing to do in inside the loop but we need to write the loop.
# we see

# for i in range(10):
   
# print('work continue.')    #expected an indented block after 'for' statement on line 31

#  we can not write like this.loop statements need some work.That why use pass
for i in range(5):
    pass
print('Work now ')

