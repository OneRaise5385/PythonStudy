'''
关于闰年！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
规定，公历年份是整百数的，必须是400的倍数的才是闰年，不是400的倍数的，虽然是4的倍数，也是平年。
这就是通常所说的： 四年一闰，百年不闰，四百年再闰。 
例如，2000年是闰年，1900年则是平年。
关于闰年！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
'''
year=int(input('请输入年份：'))
if year%400==0 or (year%4==0 and year%100!=0):
    print(year,'年是闰年')
else:
    print(year,'年不是闰年')