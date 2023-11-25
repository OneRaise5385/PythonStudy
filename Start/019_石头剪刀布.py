from random import randint
idx=0
while True:
    x=randint(1,3)
    if x==1:
        machine='石头'
    elif x==2:
        machine='剪刀'
    elif x==3:
        machine='布'
    man=input('请出拳:')
    list=['石头','剪刀','布']
    if man not in list:
        print('出拳无效,请重试')
        idx-=1
    elif man==machine:  #平局
        print('计算机出了',machine,'平局,请继续出拳')
        idx-=1
    elif (man=='石头' and machine=='剪刀') or (man=='剪刀' and machine=='布') \
        or (man=='布' and machine=='石头'):  #你赢
        print('计算机出了:',machine,'你赢了!')
    elif (man=='石头' and machine=='布') or (man=='剪刀' and machine=='石头') \
        or (man=='布' and machine=='剪刀'):  #计算机赢
        print('计算机出了:',machine,'你输了!')
    idx+=1
    if idx==3:
        print('游戏结束!')
        break