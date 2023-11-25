# 传递列表
def greet_users(names):
    '''向列表中的每位用户都发出简单的问候'''
    for name in names:
        print('Hello ' + name.title() + ' !')
        print()
guests = ['zhang','wang','li','zhao']
greet_users(guests)

# 在函数中修改列表（这个修改是永久的）
def print_models(uncomplated_models,complated_models):
    while uncomplated_models:
        pritning_model = uncomplated_models.pop()
        print(pritning_model + ' is printing.')
        complated_models.append(pritning_model)
    print(uncomplated_models)
    print(complated_models)

a = ['zhang','wang','li','zhao']
b = []
print_models(a,b)
print('---------')
print(a)
print(b)

# 禁止函数修改列表(将传入的列表参数加上切片[:],以创建该列表的副本)
c = ['zhao','qian','sun']
d = []
print_models(c[:],d)
print(c)
print(d)

# 传递任意数量的实参
def make_pizza(*toppings):
    '''
    传递任意数量的实参
    '''
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers')

# 使用任意数量的关键字参数
def build_profile(first,last,**user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

zhangyiju_profile = build_profile('zhang','yiju',location = 'zhangzhou',gender = 'male')
print(zhangyiju_profile)