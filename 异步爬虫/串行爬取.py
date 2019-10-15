import requests
import time

urls = ['http://img.netbian.com/file/2019/0604/a629ce509cc91156612cc5af9f7aa25d.jpg',
'http://img.netbian.com/file/2019/0521/316a88e109fd06df4704e39830c10e3b.jpg',
'http://img.netbian.com/file/2019/0407/df6fe4f6f66530cd1d90a8d04e2cf6d6.jpg']

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}


def getContent(url):
	print(f'开始爬取{url}')
	res = requests.get(url=url, headers=headers)
	if res.status_code == 200:
		img_name = url.split('/')[-1]
		with open('./img/'+img_name, 'wb') as f:
			f.write(res.content)
			print(f'ok, 大小为{len(res.content)}')
start_time = time.time()
for i in urls:
	getContent(i)
print(f'用时：{time.time() - start_time}')
