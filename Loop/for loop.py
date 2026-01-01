#  For loop are used for sequential traversal.For traversing list,string,tuples etc.
# Sequential traversal means 1st then 2nd 3rd like this.
# It seems like an index number. Index numbers continue 1st 0 then 1 like this.
nums=[1,4,5,3,26,7,3,8]
for val in nums:
    print(val)

vegetables=['potato','cucumber','latis','ladyfingers']
for val in vegetables:
    print(val)

string='Chattogram' 
for str in string:
    print(str)   

tu=(1,23,4,6,5,7,8,9) 
for t in tu:
    print(t)   

# we can use else with for loop in the end.It's completely optional.If you do something When loop complete then use else.In the else you write anything you need.

value=[1,2,3,4,5,6]
for va in value:
    print(va)
else:
    print('end')

# well,when use break these time need else

# search e letter;
string='Bangladesh'
for str in string:
    if(str == "e"):
        print('found')
        break
    print(str)
else:
    print('End')    

# when e is found the loop stop and nothing print.

string='Bangladesh'
for str in string:
    if(str == "e"):
        print('found')
        break
    print(str)

print('End')    
# see here when we  found e then "End " also print.That why use else.
# If we want to do something after the loop finishes, we write it inside the else block.