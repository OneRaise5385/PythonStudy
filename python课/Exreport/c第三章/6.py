num=int(input('请输入一个不多于五位的正数：'))
if num>=10000:
    print('这是一个五位数')
    ge=num%10
    shi=num//10%10
    bai=num//100%10
    qian=num//1000%10
    wan=num//10000
    print('个位：%d,十位：%d,百位：%d,千位：%d,万位：%d'%(ge,shi,bai,qian,wan))
elif num>=1000:
    print('这是一个四位数')
    ge=num%10
    shi=num//10%10
    bai=num//100%10
    qian=num//1000
    print('个位：%d,十位：%d,百位：%d,千位：%d'%(ge,shi,bai,qian))
elif num>=100:
    print('这是一个百位数')
    ge=num%10
    shi=num//10%10
    bai=num//100
    print('个位：%d,十位：%d,百位：%d'%(ge,shi,bai))
elif num>=10:
    print('这是一个十位数')
    ge=num%10
    shi=num//10
    print('个位：%d,十位：%d'%(ge,shi))
elif num>=0:
    print('这是一个个位数')
    print('个位：',num)