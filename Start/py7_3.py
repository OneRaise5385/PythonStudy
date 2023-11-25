# Practice
# 1
active = True
while active:
    poppings = input('please enter your popping: ')
    if poppings != 'quit':
        print(poppings + ' Entered!')
    if poppings == 'quit':
        active = False

# 2
while True:
    poppings = input(': ')
    if poppings == 'quit':
        break
    else:
        print('yes ' + poppings)
        