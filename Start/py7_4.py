# 使用while循环来处理列表和字典
unconfirmed_users = ['zhang','wang','li','zhao']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(current_user + ' is Ok!')
    confirmed_users.append(current_user)
print(unconfirmed_users)
print(confirmed_users)

while 'zhang' in confirmed_users:
    confirmed_users.remove('zhang')
print(confirmed_users)

# 使用用户输入来填充字典
responses = {}
active = True
while active:
    name = input('name: ')
    response = input('How old are you?')
    responses[name] = response
    repead = input('anyone else?')
    if repead == 'no':
        active = False
print(responses)