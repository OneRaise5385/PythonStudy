from random import *
a=[]
for i in range (10):
    a.append(randint(0,100))
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(min(a))
