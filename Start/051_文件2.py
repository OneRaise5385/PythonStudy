with open('wenjian3.txt','r+',encoding='utf-8') as f:  #+号能够将文件以读写的方式打开
    s=f.read(1)
    f.seek(0,0)
    f.write('1')
    f.flush()  # 将缓存区的内容写入
    s=f.read(1)  # 将指针放在最后
    f.write('2')


    