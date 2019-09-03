import requests
import re
import os

if not os.path.exists('./qiutu'):
	os.mkdir('./qiutu')
# url = 'https://www.qiushibaike.com/pic/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}
for i in range(1, 2):
	url = f'https://www.qiushibaike.com/pic/page/{i}/?s=5224191'
	response = requests.get(url=url, headers=headers).text
	ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?></div>'
	data_list = re.findall(ex, response, re.S)
	for src in data_list:
		src = 'https:' + src
		img_data = requests.get(src, headers).content
		img_name = src.split('/')[-1]
		with open('./qiutu/'+img_name, 'wb') as fp:
			fp.write(img_data)
			print(img_name, 'ok')
