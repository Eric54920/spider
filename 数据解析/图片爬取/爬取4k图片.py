from gevent import monkey;monkey.patch_all()
import gevent
import requests
from lxml import etree
import os

url = 'http://pic.netbian.com/4kfengjing/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

def download(href, name):
	img = requests.get(url=href, headers=headers).content
	img_path = './img/' + name + '.jpg'
	with open(img_path, 'wb') as f:
		f.write(img)

response = requests.get(url=url, headers=headers).text
tree = etree.HTML(response)
li_list = tree.xpath('//div[@class="slist"]//li')
if not os.path.exists('./img'):
	os.mkdir('./img')
task = []
for li in li_list:
	img_href = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
	img_name = li.xpath('./a/b/text()')[0]
	img_name = img_name.encode('ISO-8859-1').decode('gbk')
	g = gevent.spawn(download, img_href, img_name)
	task.append(g)
gevent.joinall(task)
print('over')


