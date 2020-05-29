#biggest number among three inputs
def biggest(a,b,c):
    if a>b and a>c:
       return a
    else:
       if b>a and b>c:
          return b
       else:
          return c

print(biggest(6,2,3))
print(biggest(6,2,7))
print(biggest(6,9,3))

#alternative
def big(a,b,c):
    return max(a,b,c)

print(big(45,32,23))
      

