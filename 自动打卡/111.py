import urllib3

# 发送请求实例
http = urllib3.PoolManager()

# 网址
url='http://www.jd.com'

# 请求头
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}#注释1
# 超时时间
tm = urllib3.Timeout(connect=1.0, read=3.0)
# 重试次数和重定向次数设置并生成请求
rq = http.request('GET', url=url, headers=head, timeout=tm, retries=5, redirect=4)

print('服务器响应码：', rq.status)
print('响应实体：', rq.data.decode('utf-8'))#注释2
