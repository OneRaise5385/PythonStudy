#输出
a,b,c=1,2,3  # 这样同时赋值
print(1,2,3,4,sep='@')      #设置@为分隔符号
print('格式化文本%d:%d就是格式化文本%d'%(a,b,c))
'''
变量
变量名相同，变量的标识也不相同
严格区分大小写
'''
r=1.5
print(id(r))
r=2.6
print(id(r))
# 使用变量
print('-----使用变量-----')
my_name='Jack'
print(my_name)
school_name='zzu'
print(school_name)  # 代码是自上而下一次执行的
f1=1
f2=2
f1,f2=f2,f1  # 这样实现两个数相交换

