#factorial of a number by iteration
x = int(input("enter the number: "))
def fact(x):
    i = 1
    while x>0:
        i = i*x
        x = x-1
    print(i)

fact(x)


#alternative
def factorial(n):
    i = 1
    while n>=1:
       i = i*n
       n = n-1
    return i

print(factorial(4))
