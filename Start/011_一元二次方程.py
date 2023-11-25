import math
a,b,c=eval(input('请分别输入a，b，c，中间用英文逗号隔开'))
a=float(a)
b=float(b)
c=float(c)
delta=b**2-4*a*c
delta=float(delta)
if a==0:
    print('这是一元一次方程，结果为',-c/b)
else:
    if delta>0:
        x1=(-b+math.sqrt(delta))/2/a
        x2=(-b-math.sqrt(delta))/2/a
        print('方程有两个不相等的实数根，分别是：',x1,x2)
    elif delta==0:
        x=-b/2/a
        print('方程有两个相等的实数根：',x)
    elif delta<0:
        print('方程没有实数根！')