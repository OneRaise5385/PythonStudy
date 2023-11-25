#百钱买百鸡问题
cock=0          #首先赋值
while cock<=20:         #公鸡的数量不会大于20
    hen=0
    while hen<=33:          #母鸡的数量不会大于33
        chick=100-cock-hen          #剩下的是小鸡的数量
        if cock*5+hen*3+chick/3==100:           #满足百钱的条件
            print('公鸡=%d,母鸡=%d,小鸡=%d'%(cock,hen,chick))
        hen+=1
    cock+=1
#斐波那契数列
n=eval(input('请输入数列的项数'))
f1,f2,f3=1,1,0
print('%d\n%d'%(f1,f2),end='')
for i in range(3,n+1):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3