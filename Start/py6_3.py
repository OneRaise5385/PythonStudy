# 遍历字典
favorite_number = {
    'zhang':5,
    'wang':6,
    'li':8,
    'zhao':22,
    'sun':5
}

# 遍历所有键值对 
for name,number in favorite_number.items():
    print()
    print(name)
    print(number)
    
# 遍历所有键
for name in favorite_number.keys():
    print(name.title())
    
# 按顺序遍历所有键
for name in sorted(favorite_number.keys()):
    print(name)

# 遍历字典中的所有值
for number in set(favorite_number.values()):  # 使用set()去除重复的值
    print(number)
    
# 列表内嵌套字典
alien0 = {'color':'green','points':5}
alien1 = {'color':'yellow','points':10}
alien2 = {'color':'red','points':15}
aliens = [alien0,alien1,alien2]

for alien in aliens:
    print(alien)
for i in range(27):
    new_alien = {'color':'green','points':5}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print(len(aliens))

# 字典中储存列表
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese']
}
print(pizza['crust'])
for topping in pizza['toppings']:
    print(topping)
    
# 字典中储存字典
users = {
    'zhangyiju':{
        'first':'zhang',
        'last':'yiju',
        'location':'Zhengzhou'        
    },
    'zhangci':{
        'first':'zhang',
        'last':'ci',
        'location':'zhumadian'
    }
}

for username,user_info in users.items():
    print(username +'\n')
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    
    print('\t',full_name.title())
    print('\t',location.title())