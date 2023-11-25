def disp():
    Message(w,text=v.get()).pack()
from tkinter import *
w=Tk()
w.title('单项选择')
w.geometry('800x600+200+200')
v=StringVar()
v.set('1')
Lst=['选项1','选项2','选项3']
for i in range(3):
    Radiobutton(w,text=Lst[i],variable=v,value=str(i),command=disp()).pack()
w.mainloop()
