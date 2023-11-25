import tkinter
w=tkinter.Tk()
w.title('布局管理器')
w.geometry('600x400+200+200')
L1=tkinter.Button(w,text='张义举jujujuju')
L2=tkinter.Label(w,text='是')
L3=tkinter.Label(w,text='一个')
L4=tkinter.Label(w,text='大好人')
L1.grid(row=0,column=0,sticky=tkinter.W)
L2.grid(row=0,column=1,sticky=tkinter.E)
L3.grid(row=1,column=0,sticky=tkinter.W)
L4.grid(row=1,column=1,sticky=tkinter.W)
w.mainloop()





