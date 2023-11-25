'''
1.定义类：初始化属性，被烤和添加调料的属性，显示对象信息str
2.创建对象并调用对应的实例方法

'''
# 定义烤地瓜的类
class SweetPotato():

    # 地瓜的初始状态
    def __init__(self):
        # 时间
        self.cook_time = 0
        # 状态
        self.cook_state = '生的'
        # 调料
        self.condiments = []

    # 烤地瓜
    def cook(self,time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟'
        elif self.cook_time >= 8:
            self.cook_state = '糊'   

    # 显示状态
    def __str__(self):
        return f'时间{self.cook_time},状态{self.cook_state},调料{self.condiments}'
    
    # 添加调料
    def add_condiments(self,condiment):
        self.condiments.append(condiment)


# 创建对象并调用实例方法
sweetpotato1 = SweetPotato()
sweetpotato1.cook(2)
sweetpotato1.add_condiments('辣椒')
print(sweetpotato1)
sweetpotato1.cook(2)
print(sweetpotato1)
sweetpotato1.cook(3)
sweetpotato1.add_condiments('果酱')
print(sweetpotato1)
sweetpotato1.cook(3)
print(sweetpotato1)

