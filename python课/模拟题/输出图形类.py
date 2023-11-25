# 每列输出的数字相同
for i in range(1,6):
    print(' '*(5-i),end=' ')
    for j in range(1,2*i):
        print(2*i-1,end='')
    print()
print('----------end-----------')

# 每行输出字母递减
for i in range(1,6):
    for j in range(1,7-i):
        print(chr(j+64),end='')
    print()
print('----------end------------')
