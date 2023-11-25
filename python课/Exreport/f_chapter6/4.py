# 安装jieba库
# （这个炒鸡麻烦焯焯焯焯焯焯焯焯焯焯焯焯焯焯焯焯焯焯焯焯
# 在安装第三方模块时也有可能出现“SyntaxError: invalid syntax”这个问题
# 这时需要检查一些是否是在cmd窗口下安装，同时，要到python的安装目录里面
# 安装库的时候在C:\Users\OneRaise\AppData\Local\Programs\Python\Python310\Scripts
# 在上面这个目录上安装
'''
你的义举哥因为写这道题买了水浒传的电子版，痛失30大洋
谁看到这儿的自觉v我5毛
vx: zh1372337794
我看都谁想当白嫖怪
'''
import jieba
# 注意：写地址时用向左下的下划线，同时文件与文件夹命名时不要出现中文
with open('C:/Users/OneRaise/iCloudDrive/python_study/Exreport/f_chapter6/shuihuzhuan.txt',\
    encoding='utf-8') as fr:  # 这个地址是我电脑上的地址，你把水浒传放在哪个地址就填哪个地址
    txt=fr.read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)!=1:
        counts[word]=counts.get(word,0)+1
items=list(counts.items()) 
items.sort(key=lambda x:x[1],reverse=True)
for i in range (57):  # 输出的是57个词，这57个词中包含着前二十章出场的20个人物
    word,count=items[i]
    print('{0:<10}{1:>5}'.format(word,count))

'''
你的义举哥因为写这道题买了水浒传的电子版，痛失30大洋
谁看到这儿的自觉v我5毛
vx: zh1372337794
我看都谁想当白嫖怪
'''
