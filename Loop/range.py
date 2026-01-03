# Range functions return a sequence of numbers , starting from 0 by default,
# and increments by 1 (by default),and stops before a specified number.


# seq=range(5)
# for i in seq:
#     print(i)

# for i in range(10): #range(Stop)
#     print(i)    

# for i in range(1,8): # range(start,stop)
#     print("start and stop",i)      

# for i in range(1,12,2):  # range(start, stop ,step)
#     print('start , stop and step',i)      


# If I need to print all even number from 1 to 10
for i in range(2,11,2):
    print(i)

# If I need to print all odd number from 1 to 10
for i in range(1,10,2):
    print(i)