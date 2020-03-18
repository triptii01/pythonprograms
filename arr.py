#arrays in python
#basics

#import all the functions of array
#'*' is for all the functions
from array import *

#'i' signifies that it's an integer array
vals = array('i',[5,4,7,2])
#print the array
print(vals)


#check the type of array
print(vals.typecode)

#to know the address and size of the array
print(vals.buffer_info())

#reverse the array
vals.reverse()
print(vals)

#check the index value of the element from the array
#as the array is reversed so the values will change now
print(vals[0])

#to copy the array
newArr = array(vals.typecode, ( a for a in vals ))
for e in newArr:
   print(e)
