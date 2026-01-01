# # 1. print numbers from 1 to 100
# x=1
# while x <=100:
#     print(x)
#     x +=1
    
# # 2.Print numbers from 100 to 1
# y=100
# while y>=1:
#     print(y)
#     y -=1

# # 3.print the multiplication table of  a number n.
# n=int(input())
# i=1
# while i<=10:
#     new=n*i
#     print(new)
#     i +=1

# # 4.Print the elements of the following list using a loop:[1,4,9,16,25,36,49,64,81,100]
# list1=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<=len(list1)-1:
#     print(list1[i])
#     i+=1

# # 5.Search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100)
# list2=(1,4,9,16,25,36,49,64,81,100)
# x=int(input())
# i=0
# while i<=len(list2)-2:
#     if(x==(list2[i])):
#         print("found",i)
#     else:
#         print('not found')    
#     i +=1



# For Loop

# 6. Print the elements of the following list using a loop:
#   [1,4,9,16,25,36,49,64,81,100]
list1=[1,4,9,16,25,36,49,64,81,100]
for li in list1:
    print(li)


# 7. Search for a number x in this tuple using loop:
#   [1,4,9,16,25,36,49,64,81,100]

list2=(1,4,9,16,25,36,49,64,81,100)
x=int(input())
for li in list2:
    if(x==li):
        print("found",x)
        break
    print(li)    
