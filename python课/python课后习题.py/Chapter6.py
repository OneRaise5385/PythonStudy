# 快速生成列表
a=[x**2 for x in range(5)]  # 要加中括号
print(a)

# 字典中的key使用哈希算法可以得到一个唯一值，这个值就是保存该key对应value的地方，因此能够直接定位到value

# join()函数的使用
print(' love '.join(['a','b','c']))

# 可变参数*args传入函数是储存的类型是tuple

# 列表的一种操作,按照字符长度进行排序
b=['zhaoguozhen','zhang','zhangyi','zhangyiju']
b.sort(key=lambda b:len(str(b)),reverse=True)
print(b)

# zip()函数的使用
c=dict(zip([1,2],[88,99]))
h=list(zip([1,2],[88,99]))
print(c)
print(h)

# pop()函数，默认删除最后一个元素
e=[1,2,1,2,5,6,9]
print(e)
e.pop()
print(e)

# insert()函数的用法
f=[7,8,9]
f.insert(0,666)
print(f)

# index()函数的使用
g=[3,9,3,5,3,6,5,4,3]
print([g.index(i) for i in g if i==3])

# 一个应用
d={'math':135,'ch':120,'eng':138}
print(d)
d['phy']=90
d['math']=138
d.pop('eng')
print(d)
for key in d:
    print(key,d[key])
print(d)

# 又一个应用
user=['zhangyiju','zhaoguozhen']
password=['123','789']
for i in range(3):
    user1=input('请输入用户名：')
    if user1 in user:
        pass1=input('请输入密码')
        if user1==user[0]:
            if pass1==password[0]:
                print('恭喜你，登录成功！')
                break
            else:
                print('密码错误，请重新输入')
        elif user1==user[1]:
            if pass1==password[1]:
                print('恭喜你，登录成功！')
                break
            else:
                print('密码错误，请重新输入：')
    else:
        print('用户名错误，请重新输入：')
else:
    print('三次输入错误，请稍后重试')

# 又又又一个应用
import random
s='abcdefghijklmnopqrstuvwxyz'
ls=[]
mima=''
while len(ls)<10:
    passwd=''
    for i in range(6):
        passwd+=s[random.randint(0,len(s)-1)]
    if passwd[0] in mima:
        continue
    else:
        ls.append(passwd)
        mima+=passwd[0]
print(ls)


