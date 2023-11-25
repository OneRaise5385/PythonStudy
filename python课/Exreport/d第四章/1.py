e=0
i=1
a=1
while a>=0.00001:
    e=e+a
    a=a*(1/i)
    i=i+1
print(e)