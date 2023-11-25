def neirong():
    a=random.randint(10,21)
    for i in range(1,a+1):
        b=random.randint(10,31)
        for j in range(1,b):
            c=random.choice('qwertyuiopasdfghjklzxcvbnm')
            d=random.choice('01')
            if d=='1':
                c=c.upper()
            else:
                c=c
            f1.write(c)
        f1.write('\n')
import random
with open('D:/python/1.txt','w',encoding='utf-8') as f1:
    neirong()



