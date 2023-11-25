# 统计字符出现的次数
import random
c=[random.randint(20,100) for i in range(1000)]
# print(c)
counts={}
for i in c:
    counts[i]=counts.get(i,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1])
for i in range(len(items)):
    a,b=items[i]
    print(a,b)

# 素数
def prime(x):
    for m in range(2,x):
        if x % m ==0:
            c='n'
            break
        else:
            c='y'
        return c
for i in range(3,101):
    if prime(i)=='y':
        print(i,end=' ')
else:
    print('end')
# 