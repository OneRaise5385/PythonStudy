# while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 选择什么时候退出
note = 'Enter quit to end the program!'
message = ''
while message != 'quit':
    message = input()
    print(message)

# 使用标志
active = True
while active:
    message2 = input('please input something: ')
    if message2 == 'quit':
        active = False
    else:
        print('this:' + message2)

# 使用break推出循环
# 使用continue推出循环