f1=open('D:/python/1.txt','r',encoding='utf-8')
a=f1.read()
print(len(f1.readlines()))
x=a.lower()
y=[]
for i in x:
    if i not in y:
        y.append(i)
for j in y:
    print(j,x.count(j))







