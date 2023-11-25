def dakai(t):
    new=Tk()
    new.geometry('800x600+100+100')
    new.title('查看图片')
    gif=PhotoImage(file=t)
    L2=Label(new,image=gif)
    L2.grid(row=0,column=0)
    new.mainloop()
def get_file(filepath):
    n=1
    for i in os.listdir(filepath):
        path=os.path.join(filepath,i)
        L1=Label(w,text=path).grid(row=n,column=1)
        Btn=Button(w,command=lambda: dakai(path),text='打开这张图片')
        Btn.grid(row=n,column=2)
        print(path)
        n=n+1
        if os.path.isdir(path):
            get_file(path)
from tkinter import *
import os
# from PIL import Image, ImageTk
w=Tk()
w.geometry('800x500+600+100')
w.title('图片浏览器')
filepath='C:/Users/OneRaise/Pictures'
get_file(filepath)
w.mainloop()

