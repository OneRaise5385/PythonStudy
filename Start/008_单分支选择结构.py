score=int(input('请输入你的成绩'))
#单分支结构
if score>=90:       #判断的时候必须是数字类型的，而输入的是字符串类型
    print('恭喜你，优秀了！')
else:       #注意冒号一定要写
    print('很遗憾，你没有优秀！')
#一种简单的方法
print('优秀' if score>=90 else '没有优秀')