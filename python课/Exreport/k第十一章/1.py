import math
class Colculate:
    def __init__(self,r):
        self.r=r
    def jisuan(self):
        print(2*math.pi*self.r)
        print(math.pi*self.r**2)
        print(4*math.pi*self.r**2)
        print(4/3*math.pi*self.r**3)
banjing=int(input('请输入半径'))
a=Colculate(banjing)
a.jisuan()

