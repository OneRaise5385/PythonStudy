fac_dict={"01":"机械与动力工程学院","02":"电气工程学院","03":"化工学院","04":"土木工程学院",
"05":"水利科学与工程学院","06":"力学与安全工程学院","07":"管理工程学院",
"08":"材料科学与工程学院","09":"建筑学院","63":"口腔医学院","10":"地球科学与技术学院",
"11":"生态与环境学院","21":"数学与统计学院","22":"物理学院","23":"化学学院","24":"信息工程学院",
"31":"商学院","32":"旅游管理学院","33":"政治与公共管理学院",
"34":"信息管理学院","35":"法学院","36":"文学院","37":"外国语与国际关系学院","38":"历史学院",
"39":"马克思主义学院","40":"新闻与传播学院","41":"教育学院",
"45":"书法学院","46":"美术学院","47":"生命科学学院","48":"音乐学院","49":"体育学院(校本部)",
"51":"基础医学院","52":"公共卫生学院","53":"药学院",
"54":"护理与健康学院","90":"交换生"}
grade_list=['2021','2020','2019','2018']
while True:
    num=input('请输入学号：')
    grade=num[0:4]
    fac=num[4:6]
    if num=='0':
        break
    elif len(num)!=12:
        print('学号不是12位，请重新输入')
    elif grade not in grade_list:
        print('年级必须是2021，2020，2019，2018级，请重新输入')
    elif fac not in fac_dict:
        print('找不到相应的学院，请重新输入')
    else:
        class_=num[8:10]
        ord_=num[10:12]
        fac_name=fac_dict[fac]
        print('年级:',grade,'级')
        print('学院:',fac_name)
        print('班级:',class_,'班')
        print('序号:',ord_,'号')
