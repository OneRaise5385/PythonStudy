# 判断素数
def prime(x):
    for m in range(2,x):
        if x % m==0:
            c='n'
            break
        else:
            c='y'
        return c
for i in range(3,101):
    if prime(i)=='y':
        print(i,end=' ')
else:
    print('end')
# 判断素数+制作一个交互界面
def prime1():
    x=eval(input('输入一个大于二的整数：'))
    s=str(x)
    for m in range(2,x):
        if x%m==0:
            s+='不是素数'
            break
    else:
        s+='是素数'
    Label(w,text=s,bg='yellow',font=('华文行楷','30','bold')).pack()
from tkinter import *
w=Tk()
w.geometry('300x200+600+300')
w.title('判定素数')
Btn1=Button(w,text='判定素数',width=20,height=2,bg='grey',fg='blue',command=prime1)
Btn1.pack()
w.mainloop()



def gcd(m,n):
    r=m%n
    while r:
        m=n
        n=r
        r=m%n
    else:
        return n
x=eval(input('x'))
y=eval(input('y'))
print(x,y)
print(gcd(x,y))
