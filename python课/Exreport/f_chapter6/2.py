products=[["华为P30",6688],["wine",1488],["book",80],["Shoes",799],["MateBook",5800]]
cart=[]
print(products)
while True:
	good_num=input("请输入产品对应的编号(输入非数字程序结束):")
	judge=good_num.isdigit()
	if judge==False:
		break
	if judge==True:
		good_num=eval(good_num)
		if good_num<1 or good_num>5:
			print("商品不存在")
		else:
			num=good_num-1
			judge2=products[num] in cart
			if judge2==True:
				print("已添加到购物车")
			elif judge2==False:
				cart.append(products[num])
print(cart)
