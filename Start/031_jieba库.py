import jieba 
print(jieba.lcut('我在郑州大学学习'))
a=jieba.lcut_for_search('这是一个精确模式')
c=jieba.lcut('今天天气真好',cut_all=True)
print(a)  #返回的是一个列表
print(c)
