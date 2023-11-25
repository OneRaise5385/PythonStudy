# chr()和ord()函数
for i in range(91,97):
    print(chr(i))
print(ord('a'))
# 给出大写字母输出他的小写字母
da='B'
xiao=ord(da)+32
print('%s的小写字母为%s'%(da,chr(xiao)))
'''
chr()函数的用法：

函数返回值类型为String，其数值表达式值取值范围为0~255
返回值是当前整数对应的 ASCII 码。

ord()函数的用法：

ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
它以一个字符（长度为1的字符串）作为参数，
返回对应的 ASCII 数值，或者 Unicode 数值，
如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
'''
# int()函数
print(int('110',2))
# 正弦值和余弦值的输出
import math
x=30*math.pi/180
# x=30*3.14/180
s=math.sin(x)
c=math.cos(x)
print('%.5f'%s)
print('%.5f'%c)