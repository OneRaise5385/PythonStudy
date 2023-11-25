# 保存和读取用户生成的数据
import json

username = input('what is your name:')
filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print('i remember you ' + username + '!')