# 统计文件中字母出现的次数
zm=0
with open("C:/Users/OneRaise/iCloudDrive/python_study/模拟题/zh.txt","rt") as fp:
    st=fp.readlines()
    s=' '.join(st)
    print(s)
for i in range(len(s)):
    if s[i].isalpha():
        zm+=1
print(zm)
print('-------------end------------')

# 对文件中前6个数排序，求出前五个数中大于10的偶数的个数
s=[]
n=0
with open("C:/Users/OneRaise/iCloudDrive/python_study/模拟题/zh2.txt","rt") as fp:
    st=fp.readlines()
    st=str(st)[2:-2]
print(st)
for i in st.split():
    n=n+1
    x=int(i)
    s.append(x)
    if n>=6:
        break
s.sort()
print(s)
n=0
for i in range(5):
    if s[i]>10 and s[i]%2==0:
        n=n+1
else:
    print('大于10的偶数的个数为:',n)
print('------------end------------')

# 各位相加，统计和是奇数的个数
y=[]
t=0
with open("C:/Users/OneRaise/iCloudDrive/python_study/模拟题/zh3.txt","rt") as fp:
    string=str(fp.readlines())[2:-2]
print(string)
for i in string.split():
    x=int(i)
    y.append(x)
print(y)
for m in range(5):
    mg=y[m]%10
    ms=y[m]%100//10
    mb=y[m]%1000//100
    print(mg,ms,mb)
    if (mg+ms+mb)%2==1:
        t=t+1
print(t)

