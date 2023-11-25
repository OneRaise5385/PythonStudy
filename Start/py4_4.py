# 复制列表
# 比较下面这两种复制列表的方法
# 方法一
my_foods = ['pizza','falafel','carrot']
friend_foods = my_foods
print(my_foods)
print(friend_foods)
print(id(my_foods))
print(id(friend_foods))
# 方法二
my_foods = ['pizza','falafel','carrot']
friend_foods = my_foods[:]  # 用切片复制
print(my_foods)
print(friend_foods)
print(id(my_foods))
print(id(friend_foods))

# Practice
print(my_foods[:1])
print(my_foods[1:])