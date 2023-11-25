'''
这个少了好多字
这个少了好多字
这个少了好多字
'''
def btn_click(x):
    print(x)
    result0.set(result0.get()+x)
def jisuan():
    result=result0.get()
    print(eval(result))
    result0.set(eval(result))
def clear():
    result0.set('')
    
from tkinter import *
c=Tk()
c.title('这是一个计算器')
c.geometry('350x270+200+200')

result0=StringVar()
result0.set('')
screen1=Label(c,textvariable=result0,height=4,font=('',12)).grid(row=1,column=4,sticky=SE,columnspan=2)

btn7=Button(c,command=lambda: btn_click('7'),text='7',width=8,height=2)
btn8=Button(c,command=lambda: btn_click('8'),text='8',width=8,height=2)
btn9=Button(c,command=lambda: btn_click('9'),text='9',width=8,height=2)
btn_jian=Button(c,command=lambda: btn_click('-'),text='-',width=8,height=2)
btn_jia=Button(c,command=lambda: btn_click('+'),text='+',width=8,height=5)

btn4=Button(c,command=lambda: btn_click('4'),text='4',width=8,height=2)
btn5=Button(c,command=lambda: btn_click('5'),text='5',width=8,height=2)
btn6=Button(c,command=lambda: btn_click('6'),text='6',width=8,height=2)
btn_cheng=Button(c,command=lambda: btn_click('*'),text='x',width=8,height=2)

btn1=Button(c,command=lambda: btn_click('1'),text='1',width=8,height=2,)
btn2=Button(c,command=lambda: btn_click('2'),text='2',width=8,height=2,)
btn3=Button(c,command=lambda: btn_click('3'),text='3',width=8,height=2,)
btn_chu=Button(c,command=lambda: btn_click('/'),text='/',width=8,height=2)
btn_deng=Button(c,command=jisuan,text='=',width=8,height=5)

btn0=Button(c,command=lambda: btn_click('0'),text='0',width=18,height=2)
btn_dian=Button(c,command=lambda: btn_click('.'),text='.',width=8,height=2)
btn_clear=Button(c,command=clear,text='C',width=8,height=2)

btn0.grid(row=5,column=1,columnspan=2)
btn1.grid(row=4,column=1)
btn2.grid(row=4,column=2)
btn3.grid(row=4,column=3)
btn4.grid(row=3,column=1)
btn5.grid(row=3,column=2)
btn6.grid(row=3,column=3)
btn7.grid(row=2,column=1)
btn8.grid(row=2,column=2)
btn9.grid(row=2,column=3)
btn_dian.grid(row=5,column=3)
btn_jia.grid(row=2,column=5,rowspan=2)
btn_jian.grid(row=2,column=4)
btn_cheng.grid(row=3,column=4)
btn_chu.grid(row=4,column=4)
btn_clear.grid(row=5,column=4)
btn_deng.grid(row=4,column=5,rowspan=2)

c.mainloop()