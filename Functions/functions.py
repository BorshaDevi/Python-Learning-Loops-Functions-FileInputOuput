# A  Function is a Block of Statements that perform a specific task.
# We use a function when we need to do the same task multiple times.
# Using functions helps us avoid repeating the same code and makes the          
# program cleaner and easier to maintain.
 

# Syntax: def function_Name(parameter1, parameter2):
#                                  #Do anything, You need to do.
#                                  return 
# function_Name(arg1,arg2)
 

# Parameter -> used in function definition
# [When we define a function, the variables written inside the parentheses are called parameters.]

# Argument -> used in function call.
# [When we call a function, the values passed inside the parentheses are called arguments.]

def calc_Num(a,b):
 sum=a+b
 print(sum)
calc_Num(4,5) # 9

def sum_value(p1,p2):
 return p1+p2
sum_value(5,6)  # if write like this , can not find anything.

# write like this
def sum_value(p1,p2):
 return p1 + p2
sum = sum_value(5,6)
print(sum) # 11
