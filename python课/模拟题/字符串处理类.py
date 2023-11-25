'''# 统计数字字符并计算累加和
string=input('字符串：')
s=0
for i in range(len(string)):
    x=string[i]
    if x.isdigit():
        s=s+int(x)
else:
    print(s)
print('--------------')

# 加密文件（rot13）
origin='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher='nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
olist=tuple(origin)
clist=tuple(cipher)
ocdict=dict(zip(olist,clist))
srcstr=input('请输入原文：')
destlist=[]
for ch in srcstr:
    destlist.append(ocdict.get(ch,ch))
print(' '.join(destlist))
'''
# 统计字符串中各种字符的个数
x=input('请输入一个字符串')
n=len(x)
i=0
zm=kg=sz=qt=0
while i<n:
    if 'A'<=x[i]<='Z' or 'a'<=x[i]<='z':
        zm=+1
    elif '0'<=x[i]<='9':
        sz+=1
    elif x[i]==' ':
        kg+=1
    else:
        qt+=1
print(zm,kg,sz,qt)
