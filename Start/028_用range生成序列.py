a=list(range(9))
print(a)
#列表生成式
b=[x*x for x in range(10)]  #在for之前加表达式
print(b)
c=[x*x for x in range(10) if x%2==1]
print(c)
#两个循环变量
d=[m+n for m in 'ab' for n in 'ef']
print(d)
#生成器
g=(x*x for x in range(9))
next(g)
next(g)
next(g)
for i in g:
    print(i,end=' ')