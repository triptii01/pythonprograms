def print_numbers(x):
      i = 1
      while i <= x:
         print(i)
         i = i+1

print_numbers(9)


#factorial of a number by iteration method
def fact(x):
    i = 1
    while x>0:
        i = x*i
        x = x-1
        print(i)

fact(4)
    
