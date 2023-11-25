# 异常

try:
    print(5/0)
except ZeroDivisionError:
    print('you can not divide by zero!')

print('Give me two numbers, and I will divide them!')
print('Enter q to quit.')

while True:
    first_number = input('\nfirst:')
    if first_number == 'q':
        break
    second_number = input('\nsecond:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('you can not divide by 0!')
    else:
        print(answer)

