# 将函数储存在模块中
from py8_2 import build_profile,make_pizza
print('-----以上的信息是上节中的内容-----')
zhangsan_profile = build_profile(
    'zhang',
    'san',
    location = 'zhumadian',
    gender = 'famale'
    )
print(zhangsan_profile)
help(make_pizza)


