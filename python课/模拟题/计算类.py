# 计算e的近似值
e,t,n=0,1,0
while 1/t>=10**(-5):
    e+=1/t
    n+=1
    t*=n
print(e)

# 计算1+（1+2）+（1+2+3）+...,求第几项时它的和超过50000
m,t,s=0,0,0
while m<=200:
    m+=1
    t+=m
    s+=t
else:
    print(s)
print('--------------end------------------')

# 计算1*2,2*3,3*4,...,n*(n+1)的前n项和  3080
su=0
for m in range(1,21):
    su=su+m*(m+1)
else:
    print(su)
print('---------------end---------------')

# 00
t,s,i=0,0,1
for m in range(200):
    t+=i
    s+=t
    i+=1
    if i>200:
        break
print(s)
# --------------------
print('zzzzzzzzzzzzzzzzzzzzzzzzzzz')
import random
while True:
    n=eval(input('随机数的个数'))
    if 2<=n<=101:
        break
ma=random.randint(10,99)
mi=random.randint(10,99)
for t in range(2,n+1):
    x=random.randint(10,99)
    print(x)
    if ma<x:
        ma=x
    if mi>x:
        mi=x
print(ma,mi)