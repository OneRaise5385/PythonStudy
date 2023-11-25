import os
def get_file(filepath):
    for i in os.listdir(filepath):
        path=os.path.join(filepath,i)
        print(path)
        if os.path.isdir(path):
            get_file(path)
filepath='C:'
get_file(filepath)
# filepath='C:' 如果输出这样目录下的所有文件的话，程序只会输出python_studu文件夹中的目录
