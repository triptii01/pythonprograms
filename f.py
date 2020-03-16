#input is divisible by 5 or 7 in a range
n = range(14, 27)

for i in n:
	if i%5==0:
		print(i," is divisible by 5")
		
	elif i%7==0:
		print(i," is divisible by 7")
	
	else:
		print(i," is invalid input")
