# 列表的基本操作
names = ['zhang','yang','zhao','li']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

message = 'Good morning,'
for i in range(4):
    print(message + names[i].title() + '!')
