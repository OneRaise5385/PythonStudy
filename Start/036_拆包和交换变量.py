#拆包，元组
def return_num():
    return 100,200
num1,num2=return_num()  #用两个变量来接受返回值
print(num1)
print(num2)
#交换变量的值
a=10
b=20
c=0  #定义第三方变量，为了临时存储a或b
c=a
a=b
b=c
print(a)
print(b)
#交换变量的值（方法二）
a,b=1,2
a,b=b,a
print(a)
print(b)
#引用
print('-----引用-----')
a=1
b=a
print(b)
print(id(a))  #相同的内存空间，这是同一个值的引用
print(id(b))
a=2
print(b)
print(id(a))  #a的值改变时，a的存储地址就发生了改变
print(id(b))
#可变数据类型列表
print('-------------')
aa=[10,20]
bb=aa
print(id(aa))
print(id(bb))
aa.append(30)  #这样修改后，列表的地址不变
print(aa)
print(id(aa))
print(id(bb))
print('-----引用当实参-----')
#引用当实参
def test1(n):
    print(n)
    n+=n
    print(n)
test1(b)



