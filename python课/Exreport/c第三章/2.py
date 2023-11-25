money=int(input('请输入缴费金额：'))
if money<200:
    print(money)
elif money>=500:
    print(money*0.8)
elif money>=200:
    print(money*0.9)