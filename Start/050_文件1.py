with open('wenjian1.txt','r',encoding='utf-8') as f1,open('wenjian2.txt','a',encoding='utf-8') as f2:
    f2.write(f1.read())  # 这样可以复制一个文件
f1.close()
f2.close()