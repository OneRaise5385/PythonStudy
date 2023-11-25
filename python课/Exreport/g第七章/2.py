# 最大公因数用辗转相除法，最小公倍数等于两数相乘再除以最大公因数
def suanfa(i,j):
    if i<j:
        i,j=j,i
    r=i%j
    while r!=0:
        i=j
        j=r
        r=i%j
    return j
a=eval(input('a='))
b=eval(input('b='))
c=eval(input('c='))
m=suanfa(a,b)
n=suanfa(b,c)
kkk=suanfa(m,n)
print(kkk)
