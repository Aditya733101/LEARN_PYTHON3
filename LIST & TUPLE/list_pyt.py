# list of python
# -> A built-in data type that stores set of values
# -> it can store elements of differnet type(integer,float,string,etc)
# ->list mutatble that means list change value after assign 
# -> list are used to store multiple item in singe variable 
# example - 1
# marks = ["12","34","45","67","78"]
# print(marks) 
name = ["12", "13", "14"]
print(name[1])
name[1] = "30"
print(name)
# if iterate from last index -
print(name[-1])

# ------------------------------------------------------------------------
#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 
print(thislist[:4])
if "apple" in thislist:
    print("yes : apple is in the fruite list")
