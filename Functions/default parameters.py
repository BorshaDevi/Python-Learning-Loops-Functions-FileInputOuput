# If we need to call a function  and I don't want to pass any arguments.
# For this ,we can mention default parameters.Run the function ,If none any arguments pass .
# And must important thing is first no-default value and then default value.It means ,
#  It can work without default of the first parameter.
# But you must write last parameter default value.[see example number 2.] 

# 1. 
def calculate_sum(a=1,b=2):
    print(a*b)
    # 2
    return a*b
calculate_sum()

# 2.
# def calculate_sum(a=1,b): #  we can not write this.
def calculate_sum(a,b=3):
    print(a*b)
    # 3
    return a*b
calculate_sum(1)