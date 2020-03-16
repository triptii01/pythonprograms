#entering the details by using class function
n = str(input("enter the name: "))
a = int(input("enter the roll number: "))

class person:
   def details(self):
      print("name: ",n,"roll number: ",a)

per1 = person()
person.details(per1)
