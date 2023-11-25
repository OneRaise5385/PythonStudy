people_total=eval(input('请输入总人数：'))
money_total=0
while people_total>0:
    people_num=eval(input('请输入人数：'))
    station_num=eval(input('请输入站数：'))
    if station_num<=4:
        money=people_num*3
    elif station_num<=9:
        money=people_num*4
    elif station_num>9:
        money=people_num*5
    print(people_num,'人坐',station_num,'站应付款',money,'元')
    money_total+=money
    people_total=people_total-people_num
print('总共',money_total)