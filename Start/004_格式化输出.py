age=19
gongzi1=300
gongzi2=50000
gongzi3=8000
print('%s的年龄是:%d岁'%('lucy',age))
#固定打印字符个数
print('%6s的工资是:%d元'%('小xio王',gongzi1))
print('%6s的工资是:%d元'%('小d张',gongzi2))
print('%6s的工资是:%d元'%('小李',gongzi3))
#搭配formar()函数进行格式化输出，使用时要注意format函数前面要用点号
print('{}是我们的计算机老师'.format('张三'))
#使用多个变量
print('{0}是我们的英语老师,她{1}岁了'.format('李四',30))       #注意逗号要用英文的逗号
print('{name}的数学成绩为:{score}分'.format(name='王五',score=100))
#在数字编号后面加上冒号，可以指定参数格式
print('圆周率是{0:.2f}'.format(3.14159))