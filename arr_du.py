#to find first duplicate value in the array
from array import *
arr = array('i',[3,4,5,3,6,4]) 
for x in range(len(arr)) :
    for y in range(x+1, len(arr)):
        if arr[y] == arr[x]:
          print(arr[y])
    break

