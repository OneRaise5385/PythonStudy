
# 第一章
'''
1.静态语言采用编译方式执行，脚本语言采用解释方式执行。
2.直接被解释执行的语言称为动态语言。而需要编译环境将程序转换为其它的编码再执行的语言称为静态语言。
3.python：脚本语言，动态语言
4.算法是指解题方案准确而完整的描述
5.结构化程序设计的原则：自顶向下，逐步求精，模块化，限制使用goto语句
6.windows系统上写的python在unix系统上仍然可以用
7.扩展库os中的方法remove（）不能删除只读属性的文件
8.pip命令也支持扩展名为.whl类型的文件直接安装python库
'''
# 第二章
'''
1.False代表0,True代表1
2.函数int(x)的结果是x的整数部分，并不是四舍五入
'''
# 第三章 选择结构
'''
1. 关于流程图
    矩形是执行框
    圆角矩形代表开始与结束
    菱形是判断框
    平行四边形代表数据的输入
2. 关键字保留字也称为关键字，指被编程语言内部定义并保留使用的标识符
3. 程序的基本控制结构有三种，分别是顺序结构、选择结构、循环结构
4. Python分支结构：不可以向已经执行过的语句部分跳转
5. ‘二分支结构组合形成多分支结构’这样的说法正确
'''
# 第四章 循环结构
'''
1. range(n,m),表示从n开始，到m-1。range(m)，表示从0开始，到m-1
2.在很多情况下，while语句和for语句可以等价使用
3.循环结构可以提高程序的复用性
'''
# 第五章 turtle库
'''
1. 颜色必须正确才能画图
2. 窗口这样设置最爽setup(800,600,600,100)
3. pencolor()
    pencolor(colorstring),颜色指定的字符串，例如"red"，“yellow”，或"#33cc8c"。
    pencolor((r, g, b)),RGB颜色。r，g和b中的每一个必须在0…colormode范围内，其中colormode是1.0或255
    pencolor(r, g, b),RGB颜色。r，g和b中的每一个 必须在0…colormode范围内。
    如果turtleshape是多边形，则使用新设置的pencolor绘制该多边形的轮廓。
4. turtle.penup()的别名有turtle.pu()和turtle.up()。
'''
# 第六章
'''
1.get()方法语法：
    dict.get(key, default=None)
    key -- 字典中要查找的键。
    default -- 如果指定键的值不存在时，返回该默认值。
2.不能用可变类型的数据作为字典的键
3.可变参数*args传入函数时储存的类型是tuple
4.add（）是向集合中添加元素而不是列表中
'''
# 第七章
'''
1.一个好的程序应该具备好的容错能力
'''
# 第八章
'''
1.用于显示说明文字的标签是Label（）
2.tkconstants也是tkinter的重要模块之一
3.错误说法：'利用tkinter进行主窗口的创建，可以在创建的同时，通过title修改主窗口的标题名'，不应该是同时
4.一个可视化界面有一个主窗口
5.表示“是否选择某个选项”的控件是checkbutton
'''
# 第九章
'''
1.以写模式打开的文件无法进读操作
2.文件对象的tell()方法用来返回文件指针的当前位置
3.二进制文件可以用记事本打开
4.文本文件也可以用二进制的方法读入
5.以读模式打开文件时，文件指针指向文件开始处
6.对文件进行读写操作之后必须显式关闭文件以确保所有内容都得到保存

'''
# 第十章
'''

'''
# 第十一章
'''

'''
# 第十二章
'''
1.Python扩展库xlrd支持对Excel 2003或更低版本Excel文件进行读的操作
2.可以使用py2exe或pyinstaller等展库把Python源程序打包成为exe文件，从而脱离Python环境Windows平台上运行
'''
# Others
'''
1.文件与文件夹名称尽量使用英文=
2.死循环可以用CTRL+c终止
3.vscode使用：Ctrl+f 查找
4.python中强制程序缩进，当一行中的内容过多时，用右下划线'\'
5.解释性语言：每个语句用到的时候才会编译，而且不会被保存起来，所以他的执行效率要低，
而且不能生成可独立执行的可执行文件，应用程序不能脱离其解释器。但是这中方式比较灵活，
可以动态地调节，修改应用程序很方便。
6. 编译性语言：把程序编译成机器语言的文件后，然后保存在电脑中，当电脑看到同样的语言后就回去查找以前编译的，
这样他的执行效率会很高。但是应用程序一旦需要修改，必须先修改源代码再重新生成新的目标文件才能执行，
只有目标文件而没有源代码，修改很不方便。



'''
# 
# 

# 
# 

