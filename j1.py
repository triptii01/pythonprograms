#searching the desired element in the array
from array import*
arr = array('i',[5,6,3,7,4,9])

val = int(input("enter the value for search : "))

k=0
for x in arr:
  if x==val:
    print("yes, it is present at index:",k)
    break

  k+=1
