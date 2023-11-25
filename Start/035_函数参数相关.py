#函数返回值的传递
def test1():
    return 50
def test2(num):
    print(num)
result=test1()
test2(result)
#函数的返回值（一些函数有两个返回值）
def return_num():
    return 1
    return 2
result1=return_num()
print(result1)  #一个函数有多个返回值时，无法返回多个，只能返回第一个返回值
def return_num2():
    return 1,2  #需要返回多个值时，这样写
result2=return_num2()
print(result2)  #结果是元组的形式
#return的后面可以返回元组，字典，列表等等

print('-----函数的参数-----')
#函数的参数一共有4中写法
#位置参数
def user_info(name,age,gender):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')
user_info('Tom',20,'男')  #定义和调用函数的个数是相同的，不相同的话是要报错的

#关键字参数
#通过‘键=值’的形式指定，可以让函数更加清晰，便于使用
def user_info2(name,age,gender):
    print(f'your name {name},your age {age},your gender {gender}')
user_info2(gender='男',age='20',name='小明') 
#位置参数和关键字参数同时存在的时候，一定要把位置参数放在前面

#缺省参数
#可以设置参数的默认值
def user_info3(name,age,gender='男'):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')
user_info3('Tom',20)  #当有默认参数时，实参与形参的个数可以不相同
user_info3('Rose',18,'女')

#不定长参数
#也叫可变参数，用于不缺定需要传递多少个参数时使用
#包裹位置传递
def user_info4(*args):  #形式参数前有一个星号，一般用*args
    print(args)
user_info4('Tom')
user_info4('Tom',18,'男')  #这两种都能正常执行
#注意，传进的所有参数都会被args变量收集，将传进的参数组合成一个元组，args是元组类型
#包裹关键字参数
def user_info5(**kwargs):  #包裹关键字用两个**
    print(kwargs)
user_info5(name='Tom')
user_info5(name='Tom',age=20,gender='男')
#2022年4月23日
def F(*x):
	return


