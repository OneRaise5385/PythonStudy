# 异常
# 失败时一声不吭

try:
    with open('zhang.txt') as file1:
        contents = file1.read()
except FileNotFoundError:
    # print('can not find it!')
    pass

# 储存数据

import json
numbers = [1,2,3,4,5]
with open('numbers.json','w') as file_json:
    json.dump(numbers,file_json)  # 将数字列表存储到json文件中

with open('numbers.json') as file_json_load:
    numbers_load = json.load(file_json_load)  # 将文件列表读取到内存中
print(numbers_load)
