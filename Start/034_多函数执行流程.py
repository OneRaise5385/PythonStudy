#一个程序往往有多个函数，而且多个函数共享某些函数
glo_num=0  #声明全局变量
def test1():
    global glo_num  #声明全局变量
    glo_num=100  #修改全局变量
def test2():
    print(glo_num)
print(glo_num)
test2()  #test1在这里还没有执行
test1()  #从这一步开始，test1才开始执行
test2()  #开始改变
print(glo_num)