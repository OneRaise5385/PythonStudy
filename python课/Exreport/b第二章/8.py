num=eval(input('请输入一个三位数：'))
ge=num%10
shi=num//10%10
bai=num//100
print(num,'的个位是：%d,十位是:%d,百位是：%d'%(ge,shi,bai))