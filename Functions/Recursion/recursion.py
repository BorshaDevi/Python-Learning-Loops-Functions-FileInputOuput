# When a function calls itself repeatedly.
# recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)    
