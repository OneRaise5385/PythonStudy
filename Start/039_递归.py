# 递归是一种编程思想
# 递归的应用场景  1.遍历一个文件夹下所有的文件  2.快速排序
# 特点  1.函数内部自己调用自己  2.必须有出口
def sum_numbers(num):
    if num==1:  # 这个就是这个程序的出口，如果没有出口，就会超出最大递归深度
        return 1  # 返回值返回的位置是函数调用的位置
    else:
        return num+sum_numbers(num-1)
sum_result=sum_numbers(3)
print(sum_result)

