#bigger number between two numbers
def bigger(x,y):
    if x >= y:
       return x
    return y

print(bigger(2,7))
print(bigger(3,3)) 
print(bigger(3,2))


#return true if input value is a name of a friend starting with 'D' or 'N'
def is_friend(s):
  
        if s[0] == "D" or s[0] == "N":
            return True
        else:
            return False  

print(is_friend("David"))
print(is_friend("Fred"))
print(is_friend("Naisy"))


