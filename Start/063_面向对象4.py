# 带参数的init

# __str__()使用print打印对象时，会默认打印对象的内存地址
# 使用__str__()后，就会打印这个方法中return中的数据
# 可以显示对象的信息

# __del__()当删除对象时，python解释器也会默认调用__del__()方法

class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def print_info(self):
        print(self.width)
        print(self.height)
    
    def __str__(self):
        return 'this is the washer'

    def __del__(self):
        print(self,'已经被删除')

haier = Washer(2,2)
haier.print_info()
print(haier)

meidi = Washer(1,1)

del meidi




