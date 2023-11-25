def pr(s):
    print(s+'666')
    return(s)
m={'zhang','wang','li','zhao'}
for i in m:
    print(pr(i),end=' ')
print( )
print('------------------------------------------------')
#函数参数的作用：让程序更加灵活
def add_num1():
    result=1+2
    print(result)
    return()
add_num1()
#传入自己的数据
def add_num2(a,b):  #这里的a和b是形参
    '''求和函数'''
    result=a+b
    print(result)
    return()
add_num2(10,20)  #这里的10和20为实参
#体验函数的返回值（需要返回结果给用户的时候就要用return）,return后面是表达式
def buy():
    return '烟'  #return后面的代码不执行
goods=buy()
print(goods)
def add_num(a,b):
    return a+b
result=add_num(1,2)
print(result)
print('-----函数的说明文档-----')
#用注释说明这个函数的作用
#快速查看函数的说明，函数的说明文档
help(len)  #就是这样写,help就是查看函数的说明文档
help(add_num2)  #这样自己的函数没用函数的说明文档
#定义函数的说明文档,就在函数的下面用三引号说明
print('-----函数的嵌套调用-----')
def testB():
    print('B start')
    print('这是B函数')
    print('B end')
def testA():
    print('A start')
    testB()
    print('A end')
testA()
#函数嵌套调用
def print_line():
    print('-'*20)
def print_lines(num):
    i=0
    while i <num:
        print_line()
        i+=1
print_lines(5)
#函数计算
def sum_num(a,b,c):
    return (a+b+c)/3
result2=sum_num(1,2,3)  #将结果赋值给result2，否则将不显示
print(result2)
#变量作用域
print('-----变量作用域-----')
def testA():
    a=100  #定义局部变量
    print(a)  #函数的变量只在变量内部起作用，这样的变量为局部变量，调用后就销毁
testA()
#全局变量
a2=107033233  #定义全局变量
def testC():
    print(a2)
def testB():
    a2=108011316  #修改全局变量，局部显示，实际上全局变量不改变
    print(a2)
testC()
testB()
print(a2)  #局部变量修改后，不影响全局变量
print('-----修改全局变量-----')
def testD():
    global a2  #声明a2为全局变量
    a2=888888
    print(a2)
testD()