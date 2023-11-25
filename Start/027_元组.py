#元组内的内容不可更改
#实际应用中，尽量使用元组代替列表（如果元素不更改的情况下）
t=('a','b',[1,2])
print(t[2])
print(t[2][1])
t[2][1]=3
print(t)
#tuple()可以将列表或字符串转化为元组
m=tuple(range(0,6))
n=tuple([1,2,3])
e=tuple('zhang')
print(m)
print(n)
print(e)
#多变量赋值
x,y=4,5
x,y=y,x
print(x,y)
#多变量循环遍历
for i,j in ((1,3),(2,4),(6,9)):
    print(i,j)
print('---------------------------------------------')
#zip()函数
x=(1,2,3,'a','b')
y=(7,8,9,'c')
for i,j in zip(x,y):
    print(i,j)  #如果其中的某一个序列比较长，那么只会根据最短的序列打包
print(type(i))
print(type(x))