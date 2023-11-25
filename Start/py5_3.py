r_toppings = ['mushrooms','french fries','extra cheese']
a_toppings = ['mushrooms','olives','green peppers','pepperoni',
              'pineapple','extra cheese']
for r_topping in r_toppings:
    if r_topping in a_toppings:
        print('add' + r_topping)
    else:
        print('sorry no ' + r_topping)

users = ['zhang','wang','li','zhao','sun']
for user in users:
    if user == 'zhang':
        print('ZHANG!')
    else:
        print('hello ' + user)

users2 = ['Wu','Wang','Zhou','Zhao','Qian']
users3 = []
for user in users2:
    users3.append(user.lower())
print(users3)
for user in users2:
    if user.lower() in users:
        print('other')
    else:
        print('available')
