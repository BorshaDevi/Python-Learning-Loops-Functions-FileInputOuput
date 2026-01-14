# 1. print numbers from 1 to 100
x=1
while x <=100:
    print(x)
    x +=1
    
# 2.Print numbers from 100 to 1
y=100
while y>=1:
    print(y)
    y -=1

# 3.print the multiplication table of  a number n.
n=int(input())
i=1
while i<=10:
    new=n*i
    print(new)
    i +=1

# 4.Print the elements of the following list using a loop:[1,4,9,16,25,36,49,64,81,100]
list1=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<=len(list1)-1:
    print(list1[i])
    i+=1

# 5.Search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100)
list2=(1,4,9,16,25,36,49,64,81,100)
x=int(input())
i=0
while i<=len(list2)-2:
    if(x==(list2[i])):
        print("found",i)
    else:
        print('not found')    
    i +=1



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


# range()

# 8. print numbers from 1 to 100.
for i in range(1,101):
    print(i)
        
# 9. print numbers from 100 to 1.
for i in range(100):
    print(100-i)
for i in range(100,0,-1):
    print(i)

# 10. print the multiplication table of a number n.
n=int(input("n:"))
for i in range(1,11):
    print(n*i)

# 11. write a program to find the sum of first n natural numbers.(using while)
n=5
sum=0
i=1
while i<=n:
    sum +=i
    i +=1
print(sum)    

# 12. write a program to find the factorial  of first n  numbers.(using for)
n=5
fact=1
for i in range(1,n+1):
    fact *=i
print(fact)    
         

# 13. write a function to print the length of a list (list is the parameter)
def length(list):
    return len(list)
count=length([1,2,4,5,6,"Hello",'world'])
print(count)


# 14. write a function to print the elements of a list in a single line(list is the parameter)
def elements(value):
    print(value , end=' ')
    return 
li=[1,2,4,5,6,"Hello",'world']
elements(li[0])
elements(li[1])
elements(li[2])
elements(li[3])
elements(li[4])
elements(li[5])
elements(li[6])

def print_list(list):
    for item in list:
        print(item , end=" ")
print_list(li)       



# 15. write a  function to find the factorial of n.(n is the parameter)
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(fact)
    return
factorial(5)


# 16. write a function to convert USD to Taka.
def calcu_value(usd):
    taka=usd*120
    print(taka)
calcu_value(8)    


# 17.Write a recursive function to calculate the sum of first n natural numbers.

def sum1(n):
    if(n == 0):
        return 0
    return sum1(n-1)+n
print(sum1(10))

# 18. Write a recursive function to print all elements in a list.[Hint : use list and index as parameters]

list1=[1,2,3,4,5,6]
# 1.
def element(li,lis):
    if(li<0):
        return 
    print(lis[li] , end=' ')
    element(li-1 ,lis)
element(len(list1) - 1 ,list1)

#2.
def element(lst, index):
    if index < 0:
        return
    element(lst, index - 1)
    print(lst[index])

element(list1, len(list1) - 1)

# 3.
def elem(lists,li=0):
    if(len(lists)==li):
        return 
    print(lists[li],end='')
    elem(lists,li+1)
    
nums=[1,2,3,4]     
elem(nums)
 



t=int(input("t:"))
def fact_cal(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact
for i in range(t):
    m=int(input("m:"))
    print(fact_cal(m))


# (n-1)! *n
def reu_fun_fact(n):
        if(n==0 or n==1):
                return 1
        return reu_fun_fact(n-1) * n  
    
print(reu_fun_fact(5))



# file operation practice


# 19. Create a new file "practice.txt" using python.Add the following data in it:
"""Hi everyone"
"we are learning file I/O"
'using Java.'
"I like programming in Java."""

with open('practice.txt','w') as file:
    file.write('Hi everyone')
    file.write('\nwe are learning file I/O')
    file.write('\nusing Java.')
    file.write('\nI like programming in Java.')

# 20.Write a file replace all occurrences of 'java' with 'python' in above file.
with open('practice.txt') as f:
    data=f.read()
    print(data)
    new_data=data.replace('Java','python')
    print(new_data)
    with open('practice.txt','w') as f:
        f.write(new_data)


# 21. Search if the word 'learning' exists in the file or not.
with open('practice.txt') as f:
    data=f.read()
    if(data.find('learning') !=-1):
        print(data.find('learning'))
        print('find the learning word in the file')
    else:
        print('Not found')    

def check_for_word(n):
    with open('practice.txt') as f:
        data=f.read()
        if(data.find(n) != -1):
            print('found')
        else:
            print('Not found')    

check_for_word('learning')


# 22. write to function in which line of the file does the word "learning" occur first.Print -1 word not found.
def check_for_line(n):
    with open('practice.txt') as f:
        data=True
        new_line=1
        while data:  # loop is running 
            data=f.readline()
            if(n in data):   # in means python automatically check for us.
                print(new_line)
                return new_line
            new_line +=1  
    return -1   
check_for_line('learning')   
result=check_for_line('learning')    
print(result)  
print(check_for_line('pyq') )   


def check_for_line(n):
    new_line=1
    with open('practice.txt') as f:
         while True:
            data=f.readline()
            if not (data):
                # print(data)
                break
            if(n in data):
                print(new_line)
            new_line += 1
check_for_line('learning')    

# 23. From a file containing numbers separated by comma, print the count of even numbers.

with open ('practice.txt') as f:
    data=f.read()
    print(data)
    num=''
    for i in range(len(data)):
        if(data[i] == ','):
            print(int(num))
            num=''
        else:
            num += data[i]    

with open ('practice.txt') as f:
    data=f.read()
    print(data)
    s_data=data.split(',')
    print(s_data)
    count=0
    for i in s_data:
        if(int(i)%2 == 0):
            count +=1
    print(count)