from turtle import *
setup(800,800,60,20)
for j in range(4):
    for i in range(4):
        speed(0)
        color('black','black')
        begin_fill()
        n=1
        while n<=4:
            forward(40)
            left(90)
            n=n+1
        end_fill()
        forward(80)
    left(180)
    forward(320)
    right(90)
    forward(40)
    right(90)
    for i in range(4):
        speed(0)
        color('black','black')
        begin_fill()
        forward(40)
        n=1
        while n<=4:
            forward(40)
            left(90)
            n=n+1
        forward(40)
        end_fill()
    left(180)
    forward(320)
    right(90)
    forward(40)
    right(90)
forward(320)
right(90)
forward(320)
mainloop()