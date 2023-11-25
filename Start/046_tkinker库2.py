def disp():
    s='选择了'
    if v1.get()==1:
        s+='选项A.'
    if v2.get()==1:
        s+='选项B.'
    if v3.get()==1:
        s+='选项C.'
    Label(w,text=s).pack()
from tkinter import *
w=Tk()
w.title('张义举')
w.geometry('800x600+200+200')
v1=IntVar()
v2=IntVar()
v3=IntVar()
CB1=Checkbutton(w,variable=v1,text='选项A',command=disp)
CB2=Checkbutton(w,variable=v2,text='选项B',command=disp)
CB3=Checkbutton(w,variable=v3,text='选项C',command=disp)
CB1.pack()
CB2.pack()
CB3.pack()
m=Tk()
m.title('张义举2')
m.geometry('400x200+800+200')
w.mainloop()
m.mainloop()
help(set())


