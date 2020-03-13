#this is a tuple
t = (43,27,98)
print(t)

#unpacking the tuple
a,b,c = t
print(b)

#these are other examples of tuples 
a = (54,67,43,21,98)
b = (24,56,90,87)
print("first tuple: ",a)
print("second tuple: ",b)

#swapping the values of tuples
(a,b) = (b,a)

print("swapped valueof a: ",a)
print("swapped wvalue of b: ",b) 


#tuple can be changed by dividing it into list
t = (43,76,98,[43,21])
print("new tuple: ",t)
t[3][0] = 34
print("changed value: ",t)

#comparison operation in tuple
v = (54,76,23,98)
max(v)
