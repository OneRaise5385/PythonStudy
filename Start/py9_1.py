# 类
# 创建类
class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + ' ! 坐下!')
    def roll_over(self):
        print(self.name.title() + ' ! 打滚!')

# 根据类创建实例
my_dog = Dog('yang','20')
# 访问属性
print(my_dog.name)
# 调用方法
my_dog.sit()
# 创建多个方法
your_dog = Dog('wang',20)
print(your_dog.name)
your_dog.sit()
your_dog.roll_over()

# Practice
class Restaurant():
    def __init__(self,r_name,cuisine_type):
        self.r_name = r_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.r_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print('We are opening!')
zhang_restaurant = Restaurant('zhngzhang','chuan')
print(zhang_restaurant.r_name)
zhang_restaurant.describe_restaurant()
zhang_restaurant.open_restaurant()

# Practice2
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print('first name: ' + self.first_name.title())
        print('last name: ' + self.last_name)
    def greet_user(self):
        print('Hello ' + self.first_name.title() + self.last_name.title())

zhangyiju = User('zhang','yiju')
zhangyiju.describe_user()
zhangyiju.greet_user()
print(zhangyiju.first_name)
print(zhangyiju.last_name)

# Car类
print('------------------------------------------------')
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 设置默认值
    def get_long_name(self):
        long_name = str(str(self.year) + ' ' + self.make + ' ' + self.model)
        return long_name.title()
    def read_odometer(self):
        odometer_message = 'This car has ' + str(self.odometer_reading) + ' males on it!'
        return odometer_message
    def update_odometer(self,mileage):
        if mileage >=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Sorry, please enter correct mileage!')
    def increase_odometer(self,miles):
        self.odometer_reading += miles

my_car = Car('audi','a8',2022)
print(my_car.get_long_name())

my_car.odometer_reading = 23  # 直接修改属性的默认值
print(my_car.read_odometer())

my_car.update_odometer(25)  # 通过方法修改属性的值
print(my_car.read_odometer())

my_car.increase_odometer(100)
my_car.increase_odometer(100)
print(my_car.read_odometer())
