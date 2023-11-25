#绘制太阳花
import turtle
turtle.color('red','yellow')
turtle.begin_fill()
for i in range(9):
    turtle.forward(200)
    turtle.left(160)
turtle.end_fill()
turtle.mainloop()
