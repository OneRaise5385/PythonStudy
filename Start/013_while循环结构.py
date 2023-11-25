s=0
i=1
while i<=100:
    s=s+i
    i=i+1
print(s)
a=0
b=100
while b>=1:
    a=a+b
    b=b-1
print(a)
#while无限循环语句
n=0
while True:
    if n%2==1 and n%3==2 and n%5==4 and n%6==5 and n%7==0:
        break
    n=n+1
print(n)
#输出某人英文名字中的字母
name=input('请输入你的英文名字')
x=0
while x<len(name):
    print(name[x])
    x+=1
else:
    print('结束')
#输入密码（字母和数字的组合）
string=input('请输入密码')
i=0
while i<len(string):
    if not string[i].isalnum():
        print('密码只能是数字和字母的组合！')
        break
    i+=1
else:
    print('输入密码成功！')