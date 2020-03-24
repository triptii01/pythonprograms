#check the duplicate items in the array
from array import *
arr = array('i',[3,4,6,9,4,3,6])
for x in range(len(arr)):
     for y in range(x+1, len(arr)):
        if arr[y] == arr[x]:
           print(arr[y],"is a duplicate value.","hence, it is true at index value: ", y)
        else:
           print("false")
   
