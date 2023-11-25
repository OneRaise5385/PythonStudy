#计算结果
i=1
x=1
sum=0
while i<=10:
    x=x*i
    sum=sum+x
    i=i+1
print(sum)
#用1，2，3，4组成不重复的三位数
print('我不会!')
#打印水仙花数
for n in range(1000,10000):
    a=n//1000
    b=n//100%10
    c=n//10%10
    d=n%10
    if n==a**4+b**4+c**4+d**4:
        print(n,end=' ')
#用辗转相除法求两个数的最大公约数和最小公倍数
print('我不会*2')
#求圆周率的近似值
n=1
s=0
while i>=0.000001:
    i=1.0/(2*n-1)
    s=s+(-1)**(n+1)*i
    n=n+1
print(4*s)
#求100至999中最大的三个素数
n=999
num=0
while n>100:
    for i in range(2,n):
        if n%i==0:
            break
    if i==(n-1):
        print(n,'是素数')
        num+=1
    if num==3:
        break
    else:
        n-=2
#将空格换成一杠
for c in 'zhang yi ju':
    if c==' ':
        print('-',end='')
    else:
        print(c,end='')
#输出特殊的图形
print()
for i in range(1,5):
    for m in range(2*i-1):
        print('*',end='')
    print()