#计算1-2+3-4+5-6+7-8+9....的值
n=100
n=int(n)
s=0
for x in range(1,n+1):
    s=s+x*(-1)**(x+1)
print(s)
#for的循环
for y in range(1,11,4):
    print(y)
#遍历序列的索引
city=['北京','上海','广州']
for z in range(len(city)):
    print(z,city[z])

# 选择排序
a=[5,6,3,8,6,1]
print('original list:',a)
m=len(a)
for i in range(m-1):
    minx=i
    for j in range(i+1,m):
        if a[j]<a[minx]:
            minx=j
            a[i],a[minx]=a[minx],a[i]
print('processed list:',a)
