import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
import re
import json

url = 'http://qq.ip138.com/train/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

res = requests.get(url=url, headers=headers).text
res = res.encode('ISO-8859-1').decode('gb2312')
ex = '<a href="/train/(.*?)/">.*?</a>'
href_list = re.findall(ex, res)
detail_url = 'http://qq.ip138.com/train/'
city = []
for i in href_list:
    href = detail_url + i
    response = requests.get(url=href, headers=headers).text
    # response = response.encode('ISO-8859-1').decode('gb2312')
    ex4 = '<a href="/train/.*?">(.*?)</a>'
    name_list = re.findall(ex4, response, re.S)
    # print(name_list)
    for name in name_list:
        # print(name)
        try:
            print(str(name).encode('ISO-8859-1').decode('gb2312'))
        except Exception:
            print('###########################################  '+name)
            continue
        # city.append(name.encode('ISO-8859-1').decode('gb2312'))
# with open('city.txt', 'w', encoding='utf-8') as f:
#     f.write(city)