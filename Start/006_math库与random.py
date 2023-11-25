import math
print(math.pi)
import random
print(random.random())  # 这个随机数只是0-1内的随机数
print('随机数为：',random.randint(100,999))
print(random.choice([1,2,3,9,6,5,88]))
#计算圆的周长和面积
r=2
r=float(r)
cir=2*math.pi*r
area=math.pi*r**2
print(cir)
print('圆的面积为：',area)
#求一元二次方程组的根
a=5
b=-4
c=-1
x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
print(x1,x2)
print(2.0*2.0)


