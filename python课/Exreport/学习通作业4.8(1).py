money_total=0
people_num=1
print('提示：输入人数以及对应的站数，输完之后，程序还会提示输入，将人数和站数均输入0，即可得出总额')
while people_num>0:
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
print('总共需要',money_total,'元')