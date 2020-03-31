x = str(input("enter the string: "))

tt = x[::-1]
print("the reverse of the string is: ",tt)

if x == tt:
   print("yes, the string is palindrome")
else:
   print("no")
