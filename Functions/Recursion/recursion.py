# When a function calls itself repeatedly.
# recursive function
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)    


# recursion   => 4!= (4-1)! *4
# n!=(n-1)!*n  this is called recurence  relation.
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1) * n
print(fact(4))

def fact(n+1):
    return n
print(fact(3))