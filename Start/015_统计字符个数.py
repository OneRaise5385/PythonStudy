string=input('请输入需要统计的字符')
space_n=0
digit_n=0
alpha_n=0
other_n=0
for i in range(len(string)):
    if string[i].isspace():
        space_n+=1
    elif string[i].isdigit():
        digit_n+=1
    elif string[i].isalpha():
        alpha_n+=1
    else:
        other_n+=1
print(space_n,digit_n,alpha_n,other_n)