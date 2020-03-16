#this is a list of tuples
l = [(2,5),(1,2),(5,4),(9,3)]

#increasing order of elements according to first element of the tuple
l.sort()
print(l)

#increasing order of elements according to second element of the tuple
#using lambda fucnction
tup=[(3,8),(8,6),(7,2)]
def sorting(tup):
       tup.sort(key= lambda x: x[1])
       return tup

print(sorting(tup))

#using for loop:
tup = [(6,5),(3,7),(1,8),(3,2)]
def sort(tup):
   last = len(tup)
   for i in range(len(tup)):
       for j in range(0,last-i-1):
          if (tup[j][1]>tup[j+1][1]):
               temp = tup[j]
               tup[j] = tup[j+1]
               tup[j+1] = temp

   return tup
print(sort(tup))

