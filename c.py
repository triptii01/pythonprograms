#check whether the input is divisible by 5 or 11 or not
a = int(input("enter the value of a : "))

if a%5==0:
	print("number is divisible by 5")
elif a%11==0:
	print("number is divisible by 11")
else:
	print("number is divisible neither by 5 nor by 11")
