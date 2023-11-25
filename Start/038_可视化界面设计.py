from tkinter import *
w=Tk()
w.title('这是图片标签')
w.geometry('800x800+0+0')
#图片的格式是gif
gif=PhotoImage(file='C:/Users/OneRaise/iCloudDrive/python_study/从入门开始学/colors.png')
L1=Label(w,image=gif).pack(side='left')
w.mainloop()