a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the operation: "))

def func():
    if c==1:
      print(a+b)

    elif c==2:
      print(a-b)
   
    elif c==3:
     print(a*b)

    else:
     print("not defined value")

func()
