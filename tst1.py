#some basic functions
#find function
def find(s):
    y = s.find('au',3)
    return y

print(find("wertyuijhgfdsacvbauetyukj"))

#printing input from 1 index value
def code(x):
    return x[1:]

print(code('dsfsgfgthyju'))

#adding two inputs(whether strings or numbers)
def add(a,b):
    a = a + b
    return a

print(add('wert','ewrty'))
print(add(3,6))

#printing square of the number
def square(x):
    y = x ** 2
    return y

print(square(5))

#print sum of three numbers
def sum3(a,b,c):
    return a+b+c

print(sum3(1,2,3)) 

#adding inputs in some particular manner
def abbaize(a,b):
    return a+b+b+a

print(abbaize('a','b'))
print(abbaize('dog','cat'))








