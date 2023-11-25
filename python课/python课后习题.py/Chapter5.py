from turtle import *
# setheading(30)表示该点左上方30°
# 绝对角度的设置：setheading()
# 隐藏画笔的函数是：hideturtle()
# 显示画笔的函数是：showturtle()

# 绘制太极图
def draw(radius,color1,color2):
    width(3)
    color('black',color1)
    begin_fill()
    circle(radius/2,180)
    circle(radius,180)
    left(180)
    circle(-radius/2,180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color2,color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    up()
    left(90)
    backward(radius*0.35)
    down()
    left(90)
setup(500,500)
draw(200,'black','white')
draw(200,'white','black')
mainloop()


