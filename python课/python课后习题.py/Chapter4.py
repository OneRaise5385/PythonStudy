# 能够终端程序运行的组合键是
'''
Ctrl+C
'''
# print()函数中end=()的使用
for i in range(1,10,3):
    print(i,end=',')
print('注意输出结果最后的逗号')
# 计算1！+2！+...+10！的结果
'''
方法一：使用while循环结构
'''
a=1
b=1
total=0
while a<=10:
    b=b*a
    total+=b
    a=a+1
print(total)
'''
方法二：使用for循环语句
'''
total2=0
c=1
for i in range(1,11):
    c=c*i
    total2+=c
print(total2)
'''
方法三：使用递归
'''
def suan(n):
    if n==1:
        return 1
    else:
        return n*suan(n-1)
total3=0
for i in range(1,11): 
    total3+=suan(i)
print(total3)
# 辗转相除法求最大公因数，最小公倍数
x=18
y=15
z=x*y
if x>y:
    x,y=y,x
m=y%x
while m!=0:
    y=x
    x=m
    m=y%x
print(x,z/x)
# 求圆周率的近似值
q=1
s=0
p=1
r=1
while r>=0.000001:
    s+=p
    q=q+1
    r=1/(2*q-1)
    p=(-1)**(q+1)*r
pi=4*s
print(pi)
# 成绩排序
from random import *
t=[]
for i in range(10):
    u=randint(0,100)
    t.append(u)
print(t)
n=10
for i in range(0,n):
    maxx=i
    for j in range(i+1,n):
        if t[j]>t[maxx]:
            t[j],t[maxx]=t[maxx],t[j]
print(t)
# 输出几个图形
'''
1
'''
for i in range(1,5):
    for n in range(10-i):
        print(' ',end='')
    for m in range(2*i-1):
        print('*',end='')
    print()  #  print()默认为换行
'''
2
'''
for i in range(1,5):
    for n in range(10-i):
        print(' ',end='')
    for m in range(i):
        print(m+1,end='')
    for o in range(i-1):
        print(i-o-1,end='')  #  NB
    print()
'''
3
'''
for i in range(1,5):
    for j in range(9-2*i):
        print(chr(64+i),end='')
    print()
    
