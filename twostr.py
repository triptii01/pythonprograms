#count the number of matching characters in two strings
s = str(input("enter the first string: "))
t = str(input("enter the second string: "))

for i in s:
    for j in t:
        if j==i:
           x = t.count(j)
           print(j,x)
           break
else:
    print("nothing common")
