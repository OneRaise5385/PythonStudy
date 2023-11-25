import os
import tkinter
# 路径问题
'''
getcwd()
获取当前目录
当前目录并不是指脚本所在的目录，而是所运行脚本的目录
'''
a_path=os.getcwd()+'/images'
b_path='\Alien_invasion\images'
c_path=a_path+b_path
print('绝对路径','\n',a_path)
print('总路径','\n',c_path)
'''
listdir(path)
获取目录下的内容
'''
print('------------------------------')
print('路径下的文件','\n',os.listdir(a_path))
