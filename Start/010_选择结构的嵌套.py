import random
x=random.randint(-100,100)
y=random.randint(-100,100)
print(x,y)
if x>0:
    if y>0:
        print('(',x,y,')','在第一象限')
    else:
        print('(',x,y,')','在第四象限')
else:
    if y>0:
        print('(',x,y,')','在第二象限')
    else:
        print('(',x,y,')','在第三象限')
#在坐标轴上的情况不考虑
#应用实例之制作一个能够进行两个数相加减乘除的简易计算器
z=input('请输入一个数')
suan=input('请输入运算符号，仅限加减乘除')
suan1=['+','-','*','/']     #使用列表
w=input('请再输入一个数')
z=float(z)
w=float(w)
if suan not in suan1:
    print('只能够进行加减乘除的运算')
else:
    if suan=='+':       #注意赋值与相比较不一样分别为=，==
        print(z+w)
    elif suan=='-':
        print(z-w)
    elif suan=='*':
        print(z*w)
    elif suan=='/':
        print(z/w)