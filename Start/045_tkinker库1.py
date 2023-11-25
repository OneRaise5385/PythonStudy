def zhang():
    print('我是你爹！')
import tkinter
m=tkinter.Tk()
m.title('张义举')
m.geometry('300x150+200+200')
T1='张义举\n\
是一个\n\
大好人'
# 文本的属性必须是：字体-字号-字形，或者是：字体-字号，或者是：字体
L1=tkinter.Label(m,text=T1,font=('Arial','20'),bg='green',width=10)
# width指的是标签的宽度
anniu=tkinter.Button(m,text='不要点我',command=zhang,relief='groove',width=20)
L1.pack(side='left')
anniu.pack()
m.mainloop()