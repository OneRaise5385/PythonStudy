# 对1中的数据进行加密
yuan="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
mi="nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
yuan_list=list(yuan)
mi_list=list(mi)
mi_dict=dict(zip(yuan_list,mi_list))
with open("D:/python/1.txt","r")as f1,open("D:/python/2.txt","w")as f2:
	a=[]
	b=f1.read()
	for i in b:
		a.append(mi_dict.get(i))
	f2.write(a)
