x = [3,5,4,7]
x.append(6)
print(x)

y = [2,5,4,8,1]
y.extend([4,2,1,7])
print(y)

a = [2,3,4,5,7,9]
a.insert(0,1)
print(a)

x.pop()
print(x)
y.pop()
print(y)
a.pop()
print(a)

x.reverse()
print(x)
y.reverse()
print(y)
a.reverse()
print(a)

x.sort()
print(x)
y.sort()
print(y)
a.sort()
print(a)

import bisect
bisect.insort(x,2)
bisect.insort(y,3)
bisect.insort(a,1)
print(x)
print(y)
print(a)



