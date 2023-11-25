'''
创建文件夹 os.mkdir(文件夹名字)
删除文件夹 os.rmdir(文件夹名字)
获取当前目录 os.getcwd()
改变默认目录 os.chdir(目录)
获取目录列表 os.listdir()  获取某个文件夹下的所有文件，返回一个列表
文件重命名 rename() 
'''

import os
# 创建文件夹
# os.mkdir('aa')

# 删除文件夹
# os.rmdir('aa')

# 获取当前目录
# print(os.getcwd())

# 改变默认目录路径
# os.chdir('aa')
# os.mkdir('bb')

# 获取目录列表
# a=os.listdir('aa')
# print(a)

# 文件重命名
# os.rename('aa','aaaa')

'''
批量重命名
需求：吧文件夹所有文件重命名
1.找到所有文件，获取文件夹的目录列表-----listdir()
2.构造名字
3.重命名
'''
file_list=os.listdir()  # 找到所有文件
print(file_list)
for i in file_list:  # 构造名字
    new_name='py'+i
    break
os.rename(i,new_name)

