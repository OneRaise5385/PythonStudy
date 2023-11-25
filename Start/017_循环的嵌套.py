#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2d  '%(i,j,i*j),end=' ')
    print()


print('---------没有最后一行的print的效果--------')
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d  '%(i,j,i*j),end='')
print()


#打印100以内的素数
for i in range(2,101):
    n=2
    while n<=i-1:
        if i%n==0:
            break
        n+=1
    else:
        print(i,end=' ')