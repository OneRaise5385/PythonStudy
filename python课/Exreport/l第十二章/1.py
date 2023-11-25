from bs4 import BeautifulSoup
import requests
url='https://www.eol.cn/e_html/gk/dxpm/index.shtml'
resp=requests.post(url)
resp.encoding='utf-8'
paiming=BeautifulSoup(resp.text,'html.parser')
table=paiming.find('table')
trs=table.find_all('tr')[:101]  # 排名前100名
for tr in trs:
    tds=tr.find_all('td')
    number=tds[0].text
    name=tds[1].text
    mark=tds[2].text
    print(number,name,mark)
# 可是郑大排53哎