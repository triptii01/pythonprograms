x = "green-red-yellow-black-white"
(x.find("-"))
a = x[:5]
print(a)

(x.find("-", 6))
b = x[6:9]
print(b)

(x.find("-", 10))
c = x[10:16]
print(c)

(x.find("-", 17))
d = x[17:22]
print(d)

(x.find("-", 23))
e = x[23:]
print(e)


