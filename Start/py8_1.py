# 定义函数
def greet_user():
    print('Hello!')

# 调用函数
greet_user()

# Practice
def display_message():
    print('本章学习函数')
display_message()

# 传递实参-位置实参
def describe_pet(animal_type,pet_name = '1'):
    print()
    print('I have a ' + animal_type)
    print('Its name is ' + pet_name)
describe_pet('dog','yang')
describe_pet('cat','wang')

# 关键字实参
describe_pet(pet_name = 'li',animal_type = 'harry')

# 默认值，有默认值的参数放在最后面
describe_pet('dog')

# Practice
def make_shirt(size,style = 'red'):
    print('Your T-shirt size is ' + str(size))
    print('Your T-shirt style is ' + style)
make_shirt(185,'red')
make_shirt(180)

# 返回简单值
def formatted_name(first_name,last_name,middle_name = ''):
    '''返回整洁的名字'''
    full_name = first_name + middle_name + last_name
    return full_name.title()
a = formatted_name('zhang ','ju','yi')  #  返回值并不会自动打印出来
b = formatted_name('zhang ','ju')
print(a)
print(b)

# 返回字典
def build_person(f_name,l_name,age = ''):
    person = {'first_name':f_name,'last_name':l_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',18)
print(musician)

# 结合while函数使用
while True:
    print('Please enter your name:')
    first_name = input('first name:')
    if first_name == 'q':
        break
    last_name = input('last name')
    if last_name == 'q':
        break
    c = formatted_name(first_name,last_name)
    print('hello' + c)
