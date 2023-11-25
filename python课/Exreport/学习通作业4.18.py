'''从键盘上输入一批正整数（如果遇到负数重新输入，如果遇到0停止输入)
输出：（1）输入的正整数的平均值；
		 （2）高于平均值的正整数的个数。
'''
total=0
n=0
m=0
shu_set=[]
while True:
	shu=eval(input('请输入正整数，输入0结束'))
	if shu<0:
		print('请重新输入:')
	elif shu>0:
		total=total+shu
		shu_set.append(shu)
		n=n+1
		average=total/n
	elif shu==0:
		break
for i in shu_set:
	if i>average:
		m=m+1
print('平均数是:',average)
print('大于平均数的个数是:',m)

