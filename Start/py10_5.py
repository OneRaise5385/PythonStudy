# 向用户打招呼

import json

def greet_user():
    '''问候用户，并指出其名字，若不存在用户，则添加'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input('What is your name:')
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print('I remember you ' + username)
    else:
        print('welcome back ' + username + '!')

greet_user()

