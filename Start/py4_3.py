# 列表解析
squares = [value**2 for value in range(1,15)]
print(squares)

# Practice
for i in range(1,21):
    print(i)

numbers3 = [value for value in range(1,1000001)]
# print(numbers3)
print(min(numbers3))
print(max(numbers3))

odd_numbers = [value for value in range(1,21,2)]
print(odd_numbers)