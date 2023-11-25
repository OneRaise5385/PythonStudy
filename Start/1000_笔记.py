
#turtle库中，默认方向向东为0°
#以此类推，90°是正北方向
from turtle import *  #绘制一个五角星
pensize(5)
color('yellow','red')  #第一个颜色为画笔颜色，第二个颜色为填充颜色
begin_fill()
speed(1)  #速度，0最快，然后是10，依次减小
for i in range(5):
    forward(200)
    right(144)
end_fill()
penup()
goto(70,-140)
color('black')
write('Done',font=('Atial,20,normal'))  #设置字体属性
mainloop()
#关于序列
s=1,2,3  #这是一个元组
x=4  #这里指的是x为数字4，而不是一个元组
#元组与元组可以相加减，结果是两个元组的并集
#元组和其他不能相加减
#range()函数默认的范围是0-（）内的值减一
for i in range(10):
    print(i)
    i=i+1
#sort()与reverse()没有返回值
from random import *
a=[]
for i in range (10):
    a.append(randint(0,100)) 
print(a)
print(a.sort())
print(a.reverse())
# 不管字典有多大，查找或者插入元素的速度还是很高的,因为字典是有键的
# 而集合是无序的
# 但是字典所占的内存较小，字典用大的内存换来查找速度

#安装jieba库时：
#在安装第三方模块时也有可能出现“SyntaxError: invalid syntax”这个问题，
#这时需要检查一些是否是在cmd窗口下安装，同时，要到python的安装目录里面，
#安装库的时候在C:\Users\OneRaise\AppData\Local\Programs\Python\Python310\Scripts
#在上面这个目录上安装

# 文件与文件夹命名的时候不用中文好吧

# ？？？？？？tkinter库中的字体貌似有最大限制


