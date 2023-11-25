# 文件读取
# 读取文件时，Python自动将文本解读为字符串。
# 如果是数值，使用时应该用int函数转化为整数或者用float转化为浮点数
# 读取整个文件

with open('pytest.txt') as file_object:  # 打开文件
    contents = file_object.read()   # 读取文件
    print(contents)  # 打印文件 

# 逐行读取

with open('pytest.txt') as pytest:
    lines = pytest.readlines()
for line in lines:
    print(line.rstrip())

# 使用文件内容
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# 圆周率中包含你的生日吗

pi_mi = ''
with open('pi.txt') as pi_file:
    pi_contents = pi_file.read()
for line in pi_contents:
    pi_mi += line.rstrip()
print(len(pi_mi))
# print(pi_mi)
# birthday = input('your birthday: ')
birthday = '030118'

if birthday in pi_mi:
    print('yes')
    loc_birthday = pi_mi.find(birthday)
    print(loc_birthday)
else:
    print('no')

# 写入文件

with open('write.txt','a') as file_write:
    file_write.write('i love zzu!\n')
    file_write.write('i love yin!\n')