#用第二种方法调用库
from turtle import *
setup(650,350,200,200)
penup()
fd(-250)
pendown()
pensize(20)
pencolor('green')
seth(-40)
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(16,180)
fd(40*2/3)