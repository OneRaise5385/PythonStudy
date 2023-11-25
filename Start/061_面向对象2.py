class Washer():
    def wash(self):
        print('wash cloth')
    # 在类的里面获取实例属性
    def print_info(self):
        print(self.width)

haier = Washer()
# 添加属性：对象名.属性名 = 值
haier.width = 800
haier.heigh = 500

# 在类的外面获取实例属性
print(haier.width)
haier.wash()
haier.print_info()
