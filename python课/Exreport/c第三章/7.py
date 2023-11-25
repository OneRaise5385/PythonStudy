import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
delta=b**2-4*a*c
delta2=4*a*c-b**2
if a==0:
    print('a=0时，不是二次方程')
elif delta==0:
    print('方程有两个相同的实根')
    print((-b+math.sqrt(delta))/(2*a))
elif delta>0:
    print('方程有两个不相同的实根')
    print((-b+math.sqrt(delta))/(2*a))
    print((-b-math.sqrt(delta))/(2*a))
elif delta<0:
    print('方程有两个共轭复根')
    xubu=math.sqrt(delta2)/(2*a)
    print(-b/(2*a),'+','%.2f'%(xubu),'i')
    print(-b/(2*a),'-','%.2f'%(xubu),'i')
