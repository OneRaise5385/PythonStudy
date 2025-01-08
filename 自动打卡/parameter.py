import email
import logging
import os

# 获取需要的各个参数
username = '.'
password = '.'
code_province = '41'
code_city = '4101'
location = '河南省郑州市中原区高新区科学大道100号'
vaccine = '5'
jingdu = '113.53379869232177'
weidu = '34.82148033436095'
send_type = 'serverchan'          # send_type可选bark,serverchan,email
# send_parameter = {"host": "smtp服务器地址", "user": "邮箱登录名", "password": "邮箱密码", "receiver": "接收邮件的邮箱"}   # send_type为email时，send_parameter应为json字符串，格式为：{"host": "smtp服务器地址", "user": "邮箱登录名", "password": "邮箱密码", "receiver": "接收邮件的邮箱"}
send_parameter = 'SCT180441TT1BbwRz8C6CWAx12D9BcjDJB'
zhb_parameter = os.getenv('jksb_zhb_parameter')
logger_level = os.getenv('jksb_logger_level')
jksb_timer = os.getenv('jksb_timer')
# baidu_API_Key = os.getenv("jksb_baidu_API_Key")
# baidu_Secret_Key = os.getenv("jksb_baidu_Secret_Key")


# 检查参数是否都有值
if username is None:
    raise Exception("参数jksb_username无值")
if password is None:
    raise Exception("参数jksb_password无值")
if code_province is None:
    raise Exception("参数jksb_code_province无值")
if code_city is None:
    raise Exception("参数jksb_code_city无值")
if location is None:
    raise Exception("参数jksb_location无值")
if vaccine is None:
    raise Exception("参数jksb_vaccine无值")
if jingdu is None:
    raise Exception("参数jksb_jingdu无值")
if weidu is None:
    raise Exception("参数jksb_weidu无值")
if send_type is None:
    raise Exception("参数jksb_send_type无值")
if send_parameter is None:
    raise Exception("参数jksb_send_parameter无值")
# if baidu_API_Key is None:
#     raise Exception("参数jksb_baidu_API_Key无值")
# if baidu_Secret_Key is None:
#     raise Exception("参数jksb_baidu_Secret_Key无值")

# 设置日志等级
if logger_level == 'DEBUG':
    logger_level = logging.DEBUG
elif logger_level == 'WARNING':
    logger_level = logging.WARNING
elif logger_level == 'ERROR':
    logger_level = logging.ERROR
elif logger_level == 'INFO':
    logger_level = logging.CRITICAL
else:
    logger_level = logging.INFO


url_login = 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
header = {
    'User-Agent': '.',
    'Content-Type': 'application/x-www-form-urlencoded',
}