# 在python中，__xx__()的函数叫做魔法方法，指的是具有特殊功能的函数
# __init__()方法的作用：初始化对象，设置初始化属性


class Washer():

    # 添加实例属性
    def __init__(self):
        self.width = 800
        self.height = 500

    # 创建实例方法在类里面调用实例属性
    def print_info(self):
        print(self.width)

# 创建对象
haier = Washer()
haier.print_info()