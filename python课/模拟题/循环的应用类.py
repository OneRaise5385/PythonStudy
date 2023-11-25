# 购物车，输入0结束
carts=[]
n=input('商品号：')
while n.isdigit():
    if n in ['1','2','3','4','5']:
        if n in carts:
            print('商品已经在购物车')
        else:
            carts.append(n)
    elif n=='0':
        break
    else:
        print('商品不存在')
    print('购物车里有：',carts)
    n=input('商品号：')
# 随机产生n个两位整数，求最大最小值
import random
while True:
    n=eval(input('请输入需要产生的随机数的个数：'))
    if 2<=n<=101:
        break
ma=random.randint(10,99)
mi=random.randint(10,99)
for t in range(2,n+1,1):
    x=random.randint(10,99)
    if ma<x:
        ma=x
    if mi>x:
        mi=x
print(ma,mi)