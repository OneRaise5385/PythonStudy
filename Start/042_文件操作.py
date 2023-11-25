'''
文件操作的作用：把一些内容存储起来让程序下一次执行时直接使用，不用重新制作一份，省时省力
文件操作：打开，关闭，读，写，复制，备份
打开文件open(name,mode)
name是打开文件名字的字符串
mode设置打开文件的模式(访问模式)：只读，写入，追加，默认的模式为写入
追加新内容
'''
f=open('test.txt','a')  # a指的是访问模式为追加
f.write('Jack ')
f.close()
# 访问模式:读r，写w，追加a
# r不支持写入的
g=open('test1.txt','w')  # w指的是访问模式为写入
g.write('Rose ')
g.close()
# 读取函数read
# 文件对象.read(num),num表示从文件中读取的数据的长度，如果没有，默认为读取文件的全部
# 文件内容如果换行的话，在计算机的底层是有换行符的，回有字节的占位
f=open('test.txt','r')
print(f.read())  # 20表示读取的字节数，不写表示所有
f.close()
# readlines()
f=open('test.txt')
content=f.readlines()
print(content)
# readline()
f=open('test.txt')
con=f.readline()  # 多次调用，读取多行内容
print(con)
con=f.readline()
print(con)
# 访问模式的特点
# r,rb,r+,rb+,w,wb,w+,wb+......
'''
1.r+和w+的区别 2.文件指针对数据读取的影响
2.r没有所打开的文件时报错

'''
f2=open('test2.txt','r+')
print(f2.read())
f.close()
# seek()函数，用来移动文件指针
# 文件对象.seek(偏移量，起始位置)
# 0.文件开头，1.当前位置，2.文件结尾
f3=open('test.txt','r+')
f3.seek(8,0)  # 改变读取数据偏移位置
con3=f3.read()
print(con3)
f3.close()
# 文件备份
# 1.用户输入目标文件
old_name=input('请输入您要备份文件名')  # 后缀才是真正的文件名
print(old_name)
print(type(old_name))
# 2.规划备份文件名
# 提取后缀---找到名字中的点---名字和后缀分离  组织新名字=取名字+【备份】.后缀
index=old_name.rfind('.')
print('-----找到后缀前面的点的位置-----')
print(index)
print(old_name[:index])
print(old_name[index:])
new_name=old_name[:index]+'[备份]'+old_name[index:]
print(new_name)
# 备份文件写入数据，打开源文件和新文件---源文件读取，备份文件写入---关闭文件
oldf=open(old_name,'rb')
newf=open(new_name,'wb')
while True:
    con=oldf.read(1024)
    if len(con)==0:
        break
    newf.write(con)
oldf.close()
newf.close()
# 文件和文件夹的操作
import os
# 删除文件
# os.remove('文件名称')删除文件
# os.mkdir('文件夹名称')创建文件夹
# os.rmdir('文件夹名称')删除文件夹
# getcwd()获取目录路径
print(os.getcwd())
# chdir()改变目录路径
# 文件（文件夹）重命名 os.rename(目标文件名，新文件名)
os.rename('zzz.txt','ggg.txt')








