class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area


bed = Furniture('床',6)
sofa = Furniture('沙发',4)
ball = Furniture('篮球场',1200)

class Home():
    def __init__(self,address,area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furnitures = []

    def __str__(self):
        return f'位置{self.address},面积{self.area},剩余面积{self.free_area},家具{self.furnitures}'

    def add_furniture(self,item):
        if self.free_area >= item.area:
            self.furnitures.append(item.name)
            self.free_area -= item.area
            print(f'添加{item.name}成功')
        else:
            print(f'添加{item.name}失败')

home1 = Home('北京',1000)
home1.add_furniture(bed)
home1.add_furniture(sofa)
home1.add_furniture(ball)
print(home1)