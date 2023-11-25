# 把函数作为参数传入，这样的函数称为高阶函数，一个函数可以实现多个功能
result=abs(-10)  # 求绝对值
result2=round(1.2)  # 四舍五入
result3=round(1.9)
print(result)
print(result2,result3)
# 高阶函数的写法
def add_num(a,b,f):
    return f(a)+f(b)
result4=add_num(1.2,2.7,abs)  # 一个函数作为另一个函数的参数出现
print(result4)
# 内置高阶函数
# map(),map(func,lst)
list1=[1,2,3,4,5,6]
def func(x):
    return x**2
result=map(func,list1)
print(result)
print(list(result))
# reduce(),reduce(func,lst),func必须有两个参数
# 功能：函数计算的结果和序列的下一个数据做累积计算
# 每次func计算的结果继续和序列的下一个元素做累积计算
import functools  # 先导入模块
list2=[1,2,3,4,5,6,7,8,9]
def func(a,b):
    return a+b
result=functools.reduce(func,list2)
print(result)
# filter()，过滤
# 用于过滤序列，过滤掉不符合条件的值,留下符合条件的
def func(x):
    return x%2==0
result3=filter(func,list2)
print(list(result3))










