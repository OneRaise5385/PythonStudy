# 列表元素的修改

motocycles = ['honda','yamaha','suzuki']
print(motocycles)
motocycles[0] = 'ducadi'
print(motocycles)

# 在列表中添加元素

motocycles.append('honda')
print(motocycles)

# 创建一个空列表

empty_list = []
empty_list.append('00')
empty_list.append('01')
empty_list.append('02')
empty_list.append('03')
print(empty_list)

# 在列表中插入元素

names = ['zhang','wang','li','zhao']
names.insert(0,'sun')
print(names)

# 在列表中删除元素
# 使用del删除，使用del删除后就无法载访问被删除的元素了

del names[0]
print(names)
del names[1]
print(names)

# 使用pop()删除，删除的是最后一个元素，并且能够接着使用这个值，但是删除的元素就不再原来的列表中了

print('-------------------------')
poped_names = names.pop()
print(names)
print(poped_names)

# 使用remove()删除元素，根据元素的值删除元素

print(motocycles)
expensive = 'honda'
motocycles.remove(expensive)
print(motocycles)

# Practice

guests = ['Musk','Bezos','Jack Ma']
for i in guests:
    print('Dear ' + i + ', Would you please have dinner with me?')
not_present = 'Jack Ma'
guests.remove(not_present)
guests.append('Zhang')
for i in guests:
    print('Dear ' + i + ', Would you please have dinner with me?')

print('We had found a bigger dinner table.')
guests.insert(0,'Zhong')
guests.insert(3,'Gates')
guests.append('Buffett')
for i in guests:
    print('Dear ' + i + ', Would you please have dinner with me?')

print('I have to invest two of you')
for i in range(4):
    delete_guest = guests.pop()
    print('I am sorry, ' + delete_guest)
for i in guests:
    print(i + ', You are so luck that you are qualified to have dinner with me!')
