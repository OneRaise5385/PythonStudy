# 继承

# 父类
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

# 将实例作为属性
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        '''打印一条关于电池容量的信息'''
        print('This car has a ' + str(self.battery_size) + '-kWh battery!')
    def get_range(self):
        if self.battery_size == 70:
            ranges = 240
        elif self.battery_size == 85:
            ranges = 270
        message = 'This car can go ' + str(ranges) +' miles on a full charge.'
        print(message)

# 子类
class ElectricCar(Car):
    def __init__(self,make,model,year):
        '''初始化父类'''
        super().__init__(make,model,year)  # super将父类和子类建立连接
        self.battery = Battery()

 

my_tesla = ElectricCar('tesla','s',2016)
print(my_tesla.get_long_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Practice

class Restaurant():
    def __init__(self,r_name,r_type):
        self.r_name = r_name
        self.r_type = r_type

    def describe_restaurant(self):
        print('My restaurants name: ' + self.r_name)
        print('My restaurants type: ' + self.r_type)

    def open_restaurant(self):
        print('We are opening!')

class IceCreamStand(Restaurant):
    def __init__(self,r_name,r_type):
        super().__init__(r_name,r_type)
        self.flavors = ['chocolate','cream','sweet potato','green tea']

    def show_flavors(self):
        for i in self.flavors:
            print('We have ' + i.title() + ' ice-cream!')
            
ic_parlar = IceCreamStand('Yiju-Ice-Cream','Ice-Cream-Parlar')
ic_parlar.describe_restaurant()
ic_parlar.open_restaurant()
ic_parlar.show_flavors()
