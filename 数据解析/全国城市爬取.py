import requests
from lxml import etree

url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

response = requests.get(url=url, headers=headers).text
tree = etree.HTML(response)
all_city_list = []

# 第一种方式

# # 获取热门城市
# hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
# for li in hot_li_list:
# 	city = li.xpath('./a/text()')[0]
# 	all_city_list.append(city)
# # 获取全部城市
# all_li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')

# for li in all_li_list:
# 	city = li.xpath('./a/text()')[0]
# 	all_city_list.append(city)
# print(all_city_list, len(all_city_list))

# 第二种方式

all_li_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
for li in all_li_list:
	city = li.xpath('./a/text()')[0]
	all_city_list.append(city)
print(all_city_list, len(all_city_list))


