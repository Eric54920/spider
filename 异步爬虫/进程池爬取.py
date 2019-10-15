import requests
import time
from lxml import etree
import re
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

url = 'https://www.pearvideo.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

def getContent(url):
	url = 'https://www.pearvideo.com/'+url
	# print(f'开始爬取:{url}')
	detail_res = requests.get(url=url, headers=headers).text
	tree = etree.HTML(detail_res)
	ex = 'srcUrl="(.*?)",vdoUrl'
	vid_url = re.findall(ex, detail_res)[0]
	vid_name = tree.xpath('//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1/text()')[0] + '.mp4'
	vid_data = requests.get(url=vid_url, headers=headers).content
	with open('./video/'+vid_name, 'wb') as f:
		f.write(vid_data)
		print(f'ok, 大小为{len(vid_data)}')

if __name__ == '__main__':
	urls = []
	res = requests.get(url=url, headers=headers).text
	tree = etree.HTML(res)
	li_list = tree.xpath('//*[@id="actRecommendCont"]/li')
	for i in range(3):
		li_href = li_list[i].xpath('./div/a/@href')[0]
		urls.append(li_href)
	
	start_time = time.time()
	pool = ThreadPoolExecutor(3)
	pool.map(getContent, urls)
	pool.shutdown(wait=True)
	print(f'用时{time.time() - start_time}')