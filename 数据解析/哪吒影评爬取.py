from gevent import monkey;monkey.patch_all() # 写到开头
import gevent
import requests
from lxml import etree
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

def getcontent(href):
	res = requests.get(url=href, headers=headers).text
	sub_tree = etree.HTML(res)
	title = sub_tree.xpath('//div[@class="article"]/h1/span/text()')
	print(title)

# 线程池方式
# pool = ThreadPoolExecutor(100)
# for i in range(10):
# 	url = f'https://movie.douban.com/subject/26794435/reviews?start={i*20}'
# 	response = requests.get(url=url, headers=headers).text
# 	tree = etree.HTML(response)
# 	div_list = tree.xpath('//div[@class="review-list  "]/div')
# 	for div in div_list:
# 		href = div.xpath('./div//h2/a/@href')[0]
# 		pool.submit(getcontent, href)


# 协程
for i in range(10):
	url = f'https://movie.douban.com/subject/26794435/reviews?start={i*20}'
	response = requests.get(url=url, headers=headers).text
	tree = etree.HTML(response)
	div_list = tree.xpath('//div[@class="review-list"]/div')
	task = []
	for div in div_list:
		href = div.xpath('./div//h2/a/@href')[0]
		g = gevent.spawn(getcontent, href)
		task.append(g)
	gevent.joinall(task)
print('over')












