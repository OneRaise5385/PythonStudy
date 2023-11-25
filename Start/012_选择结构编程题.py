a,b,c=eval(input('请输入三个数'))
a=int(a)
b=int(b)
c=int(c)
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)