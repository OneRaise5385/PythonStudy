from turtle import *
setup(600,400,600,100)
for i in range(6):
    color('grey','black')
    begin_fill()
    pensize(2)
    speed(10)
    forward(20)
    left(120)
    forward(20)
    left(120)
    forward(20)
    end_fill()
    penup()
    forward(20)
    left(180)
    pendown()
for j in range(6):
    speed(10)
    color('grey','black')
    begin_fill()
    forward(20)
    right(120)
    forward(20)
    right(120)
    forward(20)
    end_fill()
    penup()
    right(120)
    forward(20)
    right(60)
    pendown()
mainloop()