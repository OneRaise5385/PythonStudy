from turtle import *
import random
from wsgiref.handlers import BaseCGIHandler
screensize(300,300,'black')
speed(0)
pensize(2)
color('green','yellow')
begin_fill()
for i in range(100):
    a=360*random.random()
    b=300*random.random()
    penup()
    home()
    right(a)
    forward(b)
    pendown()
    for j in range(6):
        forward(20)
        right(144)
end_fill()
mainloop()