#this is a list
l = [4,5,2,8,1,9]
print(l)

#increasing order of elements without in-built function:
for i in range(len(l)):
   for j in range(i+1, len(l)):
       if l[i]>l[j]:
          l[i],l[j]=l[j],l[i]
          print(l)



