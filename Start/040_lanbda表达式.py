# 如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化
# lambda语法，参数可有可无，能够接受任何数量的参数，但是只能返回一个表达式
# lambda 参数列表: 表达式
# lambda 也叫“匿名函数”
def fn1():
    return 100
result=fn1()
print(result)
#应用
fn2=lambda:100
print('--注意以下两种写法的输出--')
print(fn2)  #结果是内存地址
print(fn2())
# 实现
# 使用函数
def add(a,b):
    return a+b
result=add(1,2)
print(result)
#用lambda表达式
fn1=lambda a,b: a+b
print(fn1(1,2))
# lambda的参数形式
# 1.无参数
fn1=lambda:100
print(fn1())
# 2.一个参数
fn1=lambda a:a
print(fn1(99999))
# 3.默认参数
fn1=lambda a,b,c=100:a+b+c
print(fn1(3,4))
# 可变参数*args
fn1=lambda *args:args
print(fn1(10,20,30))
# **kwargs  不定长关键字参数
fn1=lambda **kwargs:kwargs
print(fn1(name='Jack',age=20))
# 应用
# 带判断的lambda
# a和b比大小
fn1=lambda a,b:a if a>b else b
print(fn1(1000,200))
# 列表数据按字典key的值排序
student= [  # 列表内有字典
    {'name':'Tom','age':20},  # 这里一定不要忘了有逗号
    {'name':'Jack','age':19},
    {'name':'Rose','age':18}
]
student.sort(key=lambda x:x['name'])
print(student,end='')
student.sort(key=lambda x:x['name'],reverse=True)
print(student)
student.sort(key=lambda x:x['age'])
print(student)

