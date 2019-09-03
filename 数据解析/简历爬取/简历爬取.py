from gevent import monkey;monkey.patch_all()
import gevent
import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

def download(href):
	detail = requests.get(url=href, headers=headers).text
	detail = detail.encode('ISO-8859-1').decode('utf-8')
	sub_tree = etree.HTML(detail)
	src = sub_tree.xpath('//div[@class="down_wrap"]/div[2]/ul/li[1]/a/@href')[0]
	file_name = sub_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
	rar = requests.get(url=src, headers=headers).content
	filepath = './jianli/' + file_name + '.rar'
	with open(filepath, 'wb') as f:
		f.write(rar)
		print(filepath, 'ok')

lst = []
for i in range(1, 3):
	if i == 1:
		url = 'http://sc.chinaz.com/jianli/free.html'
	else:
		url = f'http://sc.chinaz.com/jianli/free_{i}.html'
	response = requests.get(url=url, headers=headers).text
	response = response.encode('ISO-8859-1').decode('utf-8')
	tree = etree.HTML(response)
	div_list = tree.xpath('//div[@id="container"]/div')
	for div in div_list:
		href = div.xpath('./a/@href')[0]
		lst.append(href)

if not os.path.exists('./jianli'):
	os.mkdir('./jianli')

task = []
for href in lst:
	g = gevent.spawn(download, href)
	task.append(g)
gevent.joinall(task)

