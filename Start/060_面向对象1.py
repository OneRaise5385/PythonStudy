# 定义类
class Washer():
    def wash(self):  # 当一个函数在class中，函数一般称为实例方法
        print('wash cloth')
        print(self)  # self指的是调用该函数的对象

# 创建对象
haier = Washer()
meidi = Washer()

# 验证成果
haier.wash()  # 调用实例方法；对象.实例方法()
print(haier)  # haier()的内存地址和self的内存地址是一样的，self指的是调用该函数的对象

# 一个类创建多个对象
meidi.wash()
print(meidi)  # 创建的多个对象的地址是不一样的

